# -*- coding: utf-8 -*-
"""
    src.api.categories
    ~~~~~~~~~~~~~~~~~~

    Functions:

        create_category
        edit_category
        get_category
        delete_category

"""
from Flask import Blueprint, request
from mongoengine.errors import NotUniqueError, ValidationError
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from src.models.category import Category
from src.models.sponsor import Sponsor


categories_blueprint = Blueprint("categories", __name__)


@categories_blueprint.route("/categories/", methods=["POST"])
def create_category():
    """
    Creates a Category
    ---
    tags:
        - category
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/Category'
        description: Created Category Object
        required: true
    responses:
        201:
            description: OK
        400:
            description: Bad request.
        409:
            description: Sorry, a category with that name already exists.
        5XX:
            description: Unexpected error.
    """
    pass


@categories_blueprint.route("/categories/", methods=["PUT"])
def edit_category():
    """
    Edits a Category
    ---
    tags:
        - category
    parameters:
        - name: name
          in: query
          type: string
          description: The name of the category.
        - name: sponsor
          in: query
          type: string
          description: The name of the sponsor.
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/Category'
        description: Updated Category Object
        required: true
    responses:
        201:
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            affected:
                                type: integer
                                description: >
                                    Number of Categories affected.
        400:
            description: Bad request.
        409:
            description: Sorry, a category with that name already exists.
        5XX:
            description: Unexpected error.
    """
    pass


@categories_blueprint.route("/categories/", methods=["DELETE"])
def delete_category():
    """
    Deletes a Category
    ---
    tags:
        - category
    parameters:
        - name: name
          in: query
          type: string
          description: The name of the category.
        - name: sponsor
          in: query
          type: string
          description: The name of the sponsor.
    responses:
        201:
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            affected:
                                type: integer
                                description: >
                                    Number of Categories affected.
        400:
            description: Bad request.
        404:
            description: Sorry, a category with that name does not exist.
        5XX:
            description: Unexpected error.
    """
    pass


@categories_blueprint.route("/categories/", methods=["GET"])
def get_category():
    """
    Gets a Category
    ---
    tags:
        - category
    parameters:
        - name: name
          in: query
          type: string
          description: The name of the category.
        - name: sponsor
          in: query
          type: string
          description: The name of the sponsor.
    responses:
        201:
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            affected:
                                type: integer
                                description: >
                                    Number of Categories affected.
        400:
            description: Bad request.
        409:
            description: Sorry, a category with that name already exists.
        5XX:
            description: Unexpected error.
    """
    pass
