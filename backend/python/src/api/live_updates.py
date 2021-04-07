# -*- coding: utf-8 -*-
"""
    src.api.live_updates
    ~~~~~~~~~~~~~~~~~~~~

    Classes:

        LiveUpdates

"""
from flask import Blueprint, request, current_app as app
from werkzeug.exceptions import BadRequest
from src.common.decorators import authenticate, privileges
from flask_socketio import Namespace, emit
from src.models.live_update import LiveUpdate

live_updates_blueprint = Blueprint("live_updates", __name__)


@live_updates_blueprint.route("/live_updates/", methods=["PUT"])
def new_update():
    """
    Adds an update
    ---
    tags:
        - live_updates
    requestBody:
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        message:
                            type: string
    responses:
        201:
            description: OK
        400:
            description: Bad Request.
        5XX:
            description: Unexpected error.
    """
    data = request.get_json()

    if not data or not data.get("message"):
        raise BadRequest()

    lup = LiveUpdate.createOne(message=data.get("message"))

    from src.tasks.socket_tasks import broadcast_ws_event
    broadcast_ws_event("new", {
        "data": lup
    }, "/liveupdates")

    res = {
        "status": "success",
        "message": "Update sent!"
    }

    return res, 201


@live_updates_blueprint.route("/live_updates/all/", methods=["DELETE"])
def delete_all_updates():
    """
    Deletes all updates
    ---
    tags:
        - live_updates
    responses:
        201:
            description: OK
    """

    LiveUpdate.drop_collection()

    from src.tasks.socket_tasks import broadcast_ws_event
    broadcast_ws_event("deleteall", namespace="/liveupdates")

    res = {
        "status": "success",
        "message": "Updates deleted!"
    }

    return res, 201


@live_updates_blueprint.route("/live_updates/<id>/", methods=["DELETE"])
def delete_update(id: int):
    """
    Deletes an Update
    ---
    tags:
        - live_updates
    parameters:
        -
            name: id
            in: path
            required: true
            schema:
                type: integer
    responses:
        201:
            description: OK
        404:
            description: Update not Found
        5XX:
            description: Unexpected error.
    """

    LiveUpdate.objects(ID=id).delete()

    from src.tasks.socket_tasks import broadcast_ws_event
    broadcast_ws_event("delete", {
        "data": id
    }, "/liveupdates")

    res = {
        "status": "success",
        "message": "Updates deleted!"
    }

    return res, 201


"""Create the SocketIO Namespace"""


class LiveUpdates(Namespace):

    def on_connect(self):
        app.logger.debug("Someone connected")
        lups = LiveUpdate.objects.exclude("id")

        self.emit("hello", lups)

    def on_disconnect(self):
        pass

    def on_reload(self, _):
        lups = LiveUpdate.objects.exclude("id")

        self.emit("reload", lups)
