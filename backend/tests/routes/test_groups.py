# flake8: noqa
import json
from src.models.hacker import Hacker
from src.models.user import ROLES
from src.models.group import Group
from tests.base import BaseTestCase


class TestGroupsBlueprint(BaseTestCase):
    """Tests for the Groups Endpoints"""

    """create_group (worked on by Conroy)"""

    def test_create_group(self):

        #create hackers to put inside group
        res1 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "conroy",
                    "email": "conroy@gmail.com",
                    "password": "fdsagfwedgasd",
                }
            ),
            content_type="application/json",
        )

        res2 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "john",
                    "email": "john@gmail.com",
                    "password": "fgnjmdsftgjh",
                }
            ),
            content_type="application/json",
        )

        res3 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "doe",
                    "email": "doe@gmail.com",
                    "password": "sdfghjk",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(res2.status_code, 201)
        self.assertEqual(res3.status_code, 201)
        self.assertEqual(Hacker.objects.count(), 3)

        #create a group
        res4 = self.client.post(
            "/api/groups/",
            data=json.dumps(
                {
                    "name" : "My Group",
                    "members" : [
                        "conroy@gmail.com", 
                        "john@gmail.com",
                        "doe@gmail.com"],
                    "categories" : [
                        "category 1",
                        "category 2",
                        "category 3"]
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res4.status_code, 201)
        self.assertEqual(Group.objects.count(), 1)

    def test_create_group_invalid_json(self):

        res4 = self.client.post(
            "/api/groups/",
            data=json.dumps({}),
            content_type="application/json",
        )

        self.assertEqual(res4.status_code, 400)
        self.assertEqual(Group.objects.count(), 0)

    def test_create_group_member_not_found(self):

        #create hackers to put inside group
        res1 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "conroy",
                    "email": "conroy@gmail.com",
                    "password": "fdsagfwedgasd",
                }
            ),
            content_type="application/json",
        )

        res2 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "john",
                    "email": "john@gmail.com",
                    "password": "fgnjmdsftgjh",
                }
            ),
            content_type="application/json",
        )

        res3 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "doe",
                    "email": "doe@gmail.com",
                    "password": "sdfghjk",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(res2.status_code, 201)
        self.assertEqual(res3.status_code, 201)
        self.assertEqual(Hacker.objects.count(), 3)

        #create a group
        res4 = self.client.post(
            "/api/groups/",
            data=json.dumps(
                {
                    "name" : "My Group",
                    "members" : [
                        "obviouslynotmyemail@gmail.com", 
                        "john@gmail.com",
                        "doe@gmail.com"],
                    "categories" : [
                        "category 1",
                        "category 2",
                        "category 3"]
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res4.status_code, 404)
        self.assertEqual(Group.objects.count(), 0)

    def test_create_group_duplicate_group(self):

        #create hackers to put inside groups
        res1 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "conroy",
                    "email": "conroy@gmail.com",
                    "password": "fdsagfwedgasd",
                }
            ),
            content_type="application/json",
        )

        res2 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "john",
                    "email": "john@gmail.com",
                    "password": "fgnjmdsftgjh",
                }
            ),
            content_type="application/json",
        )

        res3 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "doe",
                    "email": "doe@gmail.com",
                    "password": "sdfghjk",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(res2.status_code, 201)
        self.assertEqual(res3.status_code, 201)
        self.assertEqual(Hacker.objects.count(), 3)

        #create groups        
        res4 = self.client.post(
            "/api/groups/",
            data=json.dumps(
                {
                    "name" : "My Group",
                    "members" : [
                        "conroy@gmail.com", 
                        "john@gmail.com"],
                    "categories" : [
                        "category 1",
                        "category 2",
                        "category 3"]
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res4.status_code, 201)
        self.assertEqual(Group.objects.count(), 1)

        res5 = self.client.post(
            "/api/groups/",
            data=json.dumps(
                {
                    "name" : "My Group",
                    "members" : [
                        "doe@gmail.com"],
                    "categories" : [
                        "category 1",
                        "category 2",
                        "category 3"]
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res5.status_code, 409)
        self.assertEqual(Group.objects.count(), 1)

    def test_create_group_invalid_datatypes(self):

        #create hackers to put inside group
        res1 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "conroy",
                    "email": "conroy@gmail.com",
                    "password": "fdsagfwedgasd",
                }
            ),
            content_type="application/json",
        )

        res2 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "john",
                    "email": "john@gmail.com",
                    "password": "fgnjmdsftgjh",
                }
            ),
            content_type="application/json",
        )

        res3 = self.client.post(
            "/api/hackers/",
            data=json.dumps(
                {
                    "username": "doe",
                    "email": "doe@gmail.com",
                    "password": "sdfghjk",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res1.status_code, 201)
        self.assertEqual(res2.status_code, 201)
        self.assertEqual(res3.status_code, 201)
        self.assertEqual(Hacker.objects.count(), 3)

        #create a group
        res4 = self.client.post(
            "/api/groups/",
            data=json.dumps(
                {
                    "name" : 2142114,
                    "members" : [
                        "conroy@gmail.com", 
                        "john@gmail.com",
                        "doe@gmail.com"],
                    "categories" : [
                        "category 1",
                        "category 2",
                        "category 3"]
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(res4.status_code, 400)
        self.assertEqual(Group.objects.count(), 0)

    """edit_group (worked on by Conroy)"""
    
    def test_edit_group(self):

        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )

        #edit group
        res = self.client.put(
            "/api/groups/My Group/",
            data=json.dumps({"name": "My Updated Group",
                             "members": [
                                        "conroy@gmail.com", 
                                        "john@gmail.com",
                                        "doe@gmail.com"]}),
            content_type="application/json",
        )        
        
        self.assertEqual(res.status_code, 201)
          

    def test_edit_group_invalid_json(self):

        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        #edit group
        res = self.client.put(
            "/api/groups/My Group/",
            data=json.dumps({}),
            content_type="application/json",
        )        
        
        self.assertEqual(res.status_code, 400)

    def test_edit_group_not_found(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        #edit group
        res = self.client.put(
            "/api/groups/Not My Group/",
            data=json.dumps({"name": "My Updated Group",
                             "members": [
                                        "conroy@gmail.com", 
                                        "john@gmail.com",
                                        "doe@gmail.com"]}),
            content_type="application/json",
        )        
        
        self.assertEqual(res.status_code, 404)
    
    def test_edit_group_member_not_found(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        #edit group
        res = self.client.put(
            "/api/groups/My Group/",
            data=json.dumps({"name": "My Updated Group",
                             "members": [
                                        "obviouslynotmyemail@gmail.com", 
                                        "john@gmail.com",
                                        "doe@gmail.com"]}),
            content_type="application/json"
        )        
        
        self.assertEqual(res.status_code, 404)
    
    def test_edit_group_duplicate_group(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create groups
        new_group1 = Group.createOne(
            name = "Group 1",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        new_group2 = Group.createOne(
            name = "Group 2",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        #edit a group
        res = self.client.put(
            "/api/groups/Group 1/",
            data=json.dumps({"name": "Group 2",
                             "members": [
                                        "conroy@gmail.com", 
                                        "john@gmail.com",
                                        "doe@gmail.com"]}),
            content_type="application/json",
        )        
        
        self.assertEqual(res.status_code, 409)

    def test_edit_group_invalid_datatypes(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )
        
        #edit group
        res = self.client.put(
            "/api/groups/My Group/",
            data=json.dumps({"name": 1,
                             "members": [
                                        "conroy@gmail.com", 
                                        "john@gmail.com",
                                        "doe@gmail.com"]}),
            content_type="application/json",
        )        
        
        self.assertEqual(res.status_code, 400)
        
    """get_group (worked on by Conroy)"""

    def test_get_group(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )

        #get the group
        res = self.client.get("/api/groups/My Group/")
        self.assertEqual(res.status_code, 200)

    def test_get_group_not_found(self):
        
        #create hackers to put inside group
        new_hacker1 = Hacker.createOne(
            first_name = "Conroy",
            username = "conroy",
            email = "conroy@gmail.com",
            password = "dsafadsgdasg",
            roles = ROLES.HACKER
        )

        new_hacker2 = Hacker.createOne(
            first_name = "John",
            username = "john",
            email = "john@gmail.com",
            password = "fgnjmdsftgjh",
            roles = ROLES.HACKER
        )

        new_hacker3 = Hacker.createOne(
            first_name = "Doe",
            username = "doe",
            email = "doe@gmail.com",
            password = "sdfghjk",
            roles = ROLES.HACKER
        )

        #create a group
        new_group = Group.createOne(
            name = "My Group",
            members = [
                        new_hacker1, 
                        new_hacker2,
                        new_hacker3],
            categories = [
                        "category 1",
                        "category 2",
                        "category 3"]
        )

        #"get" the group
        res = self.client.get("/api/groups/Obviously Not My Group/")
        self.assertEqual(res.status_code, 404)