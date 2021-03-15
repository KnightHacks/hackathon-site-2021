# -*- coding: utf-8 -*-
"""
    src.api.sponsor
    ~~~~~~~~~~~~~~~

    Functions:

        create_sponsor()
        update_sponsor()

"""
from flask import Blueprint, request
from mongoengine.errors import NotUniqueError, ValidationError
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from src.models.sponsor import Sponsor
from src.models.user import ROLES

sponsors_blueprint = Blueprint("sponsors", __name__)


@sponsors_blueprint.route("/sponsors/", methods=["POST"])
def create_sponsor():
    """
    Creates a new Sponsor.
    ---
    tags:
        - sponsor
    summary: Create Sponsor
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/Sponsor'
        description: Created Sponsor Object
        required: true
    responses:
        201:
            description: OK
        400:
            description: Bad request.
        409:
            description: Sorry, that sponsor_name already exists.
        5XX:
            description: Unexpected error.
    """
    data = request.get_json()

    if not data:
        raise BadRequest("Not data")

    try:
        sponsor = Sponsor.createOne(**data, roles=ROLES.SPONSOR)
    except NotUniqueError:
        raise Conflict("Sorry, this sponsor already exists.")
    except ValidationError:
        raise BadRequest("Validation Error")

    """Send Verification Email"""
    token = sponsor.encode_email_token()
    from src.common.mail import send_verification_email
    send_verification_email(sponsor, token)

    res = {
        "status": "success",
        "message": "Sponsor was created!"
    }

    return res, 201


@sponsors_blueprint.route("/sponsors/delete_sponsor/<sponsor_name>/", methods=["DELETE"])
def delete_sponsor(sponsor_name: str):
    """
    Deletes an existing Sponsor.
    ---
    tags:
        - sponsor
    summary: Delete Sponsor
    parameters:
        - id: sponsor_name
          in: path
          description: Sponsor name
          required: true
          schema:
            type: string
    responses:
        201:
            description: OK
        400:
            description: Bad request.
        409:
            description: Sorry, that sponsor_name already exists.
        5XX:
            description: Unexpected error.
    """

    sponsor = Sponsor.objects(sponsor_name=sponsor_name)

    if not sponsor:
        raise NotFound("The specified sponsor does not exist in the database.")

    sponsor.delete()

    res = {
        "status": "success",
        "message": "Sponsor was deleted!"
    }

    return res, 201


@sponsors_blueprint.route("/sponsors/<sponsor_name>/", methods=["GET"])
def get_sponsor(sponsor_name: str):
    """
    Retrieves a sponsor's information using their name.
    ---
    tags:
        - sponsor
    summary: Gets a sponsor's information from their name.
    parameters:
        - name: sponsor_name
          in: path
          type: string
          description: The sponsor's information.
          required: true
    responses:
        200:
            description: OK

    """
    sponsor = Sponsor.objects(sponsor_name=sponsor_name).exclude(
        "date",
        "email_token_hash",
        "id")

    if not sponsor:
        raise NotFound()
    
    res = {
        "Sponsor": sponsor,
        "status": "success"
    }

    print(res)

    return res, 200


@sponsors_blueprint.route("/sponsors/<sponsor_name>/", methods=["PUT"])
def edit_sponsor(sponsor_name: str):
    """
    Updates a sponsor
    ---
    tags:
        - sponsor
    summary: Updates a sponsor
    parameters:
        - id: sponsor_name
          in: path
          description: The name of the sponsor to be updated.
          required: true
          schema:
            type: string
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/Sponsor'
    responses:
        201:
            description: OK
        400:
            description: Bad Request
        404:
            description: Sponsor doesn't exist
        5XX:
            description: Unexpected error.
    """
    update = request.get_json()
    if not update:
        raise BadRequest()
    
    sponsor = Sponsor.objects(sponsor_name=sponsor_name)
    if not sponsor:
        raise NotFound()

    try:
        sponsor.update(**update)
    except NotUniqueError:
        raise Conflict("Sorry, a sponsor already exists with that name.")
    except ValidationError:
        raise BadRequest()

    res = {        
        "status": "success",
        "message": "Sponsor successfully updated."
    }
    return res, 201
