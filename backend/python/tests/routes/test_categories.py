# flake8: noqa
import json
from src.models.category import Category
from src.models.user import ROLES
from src.models.sponsor import Sponsor
from tests.base import BaseTestCase


class TestCategoriesBlueprint(BaseTestCase):
    """Tests for the categories Endpoints"""

    """create_category"""
    def test_create_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")

        res = self.client.post(
            "/api/categories/",
            data=json.dumps({
                "name": "new_category",
                "sponsor": "new_sponsor",
                "description": "new_description"
            }),
            content_type="application/json")

        self.assertEqual(res.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)

    def test_create_category_invalid_json(self):
        res = self.client.post(
            "/api/categories/",
            data=json.dumps({}),
            content_type="application/json"
        )

        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["name"], "Bad Request")
        self.assertEqual(Category.objects.count(), 0)

    def test_create_category_sponsor_not_found(self):
        res = self.client.post(
            "/api/categories/",
            data=json.dumps({
                "name": "new_category",
                "sponsor": "random_sponsor1",
                "description": "new_description"
            }), 
            content_type="application/json")

        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["name"], "Not Found")
        self.assertEqual(Category.objects.count(), 0)


    def test_create_category_duplicate_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        res = self.client.post(
            "/api/categories/",
            data=json.dumps({
                "name": "new_category",
                "sponsor": "new_sponsor",
                "description": "new_description"
            }),
            content_type="application/json")
        
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 409)
        self.assertIn("Sorry, a category with that name already exists.", data["description"])
        self.assertEqual(Category.objects.count(), 1)

    def test_create_category_invalid_datatypes(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")

        res = self.client.post(
            "/api/categories/",
            data=json.dumps({
                "name": "new_category",
                "sponsor": "new_sponsor",
                "description": 123456
            }),
            content_type="application/json")
        
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["name"], "Bad Request")
        self.assertEqual(Category.objects.count(), 0)

    """edit_category"""
    def test_edit_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        res = self.client.put(
            "/api/categories/?name=new_category",
            data=json.dumps({
                "name": "another_category"
            }),
            content_type="application/json")

        self.assertEqual(res.status_code, 201)

        updated = Category.findOne(name="another_category")

        self.assertEqual(updated.name, "another_category")

    def test_edit_category_sponsor_not_found_query(self):
        pass

    def test_edit_category_not_found(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@sponsor.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")

        res = self.client.put(
            "/api/categories/?name=new_category&sponsor=new_sponsor",
            data=json.dumps({
                "name": "another_category"
            }),
            content_type="application/json")
        
        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["name"], "Sorry, no categories exist that match the query.")

    def test_edit_category_sponsor_not_found_update(self):
        pass

    def test_edit_category_duplicate_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@sponsor.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")
        Category.createOne(name="another_category",
                           sponsor="new_sponsor",
                           description="new_description")

        res = self.client.put(
            "/api/categories/?name=new_category&sponsor=new_sponsor",
            data=json.dumps({
                "name": "another_category"
            }),
            content_type="application/json")

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 409)
        self.assertEqual(data["description"], "Sorry, a category with that name already exists.")

    def test_edit_category_invalid_datatypes(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@sponsor.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        res = self.client.put(
            "/api/categories/?name=new_category&sponsor=new_sponsor",
            data=json.dumps({
                "description": 123456
            }),
            content_type="application/json")

        data = json.loads(res.data.decode())

        # self.assertEqual(res.status_code, 400)
        self.assertEqual(data["name"], "Bad Request")

    """delete_category"""
    def test_delete_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        token = self.login_user(ROLES.ADMIN)

        res = self.client.delete("/api/categories/?name=new_category&sponsor=new_sponsor",
                                 headers=[("sid", token)])

        # self.assertEqual(res.status_code, 201)
        self.assertEqual(Category.objects.count(), 0)

    def test_delete_category_sponsor_not_found(self):
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        token = self.login_user(ROLES.ADMIN)

        res = self.client.delete("/api/categories/?name=new_category&sponsor=new_sponsor",
                                 headers=[("sid", token)])
        
        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 404)
        self.assertIn("A sponsor with that name does not exist!", data["description"])
        self.assertEqual(Category.objects.count(), 1)

    def test_delete_category_not_found(self):
        token = self.login_user(ROLES.ADMIN)

        res = self.client.delete("/api/categories/?name=new_category",
                                 headers=[("sid", token)])
        
        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 404)
        self.assertIn("Sorry, no categories exist that match the query.", data["description"])
        self.assertEqual(Category.objects.count(), 0)

    """get_category"""
    def test_get_category(self):
        Sponsor.createOne(username="new_sponsor",
                          email="new@email.com",
                          password="new_password",
                          roles=ROLES.SPONSOR,
                          sponsor_name="new_sponsor")
        cat = Category.createOne(name="new_category",
                                 sponsor="new_sponsor",
                                 description="new_description")

        res = self.client.get("/api/categories/?name=new_category&sponsor=new_sponsor")

        data = json.loads(res.data.decode())
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(cat.name, data["categories"]["name"])
        self.assertEqual(cat.sponsor, data["categories"]["sponsor"])
        self.assertEqual(cat.description, data["categories"]["description"])

    def test_get_category_sponsor_not_found(self):
        Category.createOne(name="new_category",
                           sponsor="new_sponsor",
                           description="new_description")

        res = self.client.get("/api/categories/?name=new_category&sponsor=new_sponsor/")

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 404)
        self.assertIn("A sponsor with that name does not exist!", data["description"])

    def test_get_category_not_found(self):
        res = self.client.get("/api/categories/?name=new_category/")

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 404)
        self.assertIn("Sorry, no categories exist that match the query.", data["description"])
