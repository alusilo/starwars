import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.
class PlanetTestCase(TestCase):
    
    __username = "test_user"
    __email = "test_email@test.test"
    __password = "test_passwd"
    def setUp(self):
        user = User(
            username=self.__username,
            email=self.__email,
        )
        user.set_password(self.__password)
        user.save()
    
    def test_request_token(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in content.keys())

    def test_create_planet(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        data = {
            "name": "Test Planet",
            "description": "Test description of Test Planet."
        }
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = client.post("/planets/", data, format="json")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_read_planet(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        data = {
            "name": "Test Planet",
            "description": "Test description of Test Planet."
        }
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = client.post("/planets/", data, format="json")
        content = json.loads(response.content)

        response = client.get(f"/planets/{content['id']}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("description" in content.keys())

    def test_update_planet(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        data = {
            "name": "Test Planet",
            "description": "Test description of Test Planet."
        }
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = client.post("/planets/", data, format="json")
        content = json.loads(response.content)

        data = {
            "name": "Test Planet Modified",
            "description": "Test description of Test Planet Modified."
        }
        response = client.put(f"/planets/{content['id']}/", data, format="json")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_delete_planet(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        data = {
            "name": "Test Planet",
            "description": "Test description of Test Planet."
        }
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = client.post("/planets/", data, format="json")
        content = json.loads(response.content)

        response = client.delete(f"/planets/{content['id']}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
