# flake8: noqa
import json
from tests.base import BaseTestCase
from src import socketio


class TestLiveUpdatesBlueprint(BaseTestCase):
    """Tests for the LiveUpdates Endpoints"""

    # TODO: Figure out if this works or if I don't need to do this thing
    def setUp(self):
        self.wsclient = socketio.test_client(
            namespace="/liveupdates",
            flask_test_client=self.client
        )

    """new_update"""
    def test_new_update(self):
        pass

    def test_new_update_invalid_json(self):
        pass

    """delete_all_updates"""
    def test_delete_all_updates(self):
        pass

    """delete_update"""
    def test_delete_update(self):
        pass
