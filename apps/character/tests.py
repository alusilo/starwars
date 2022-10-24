import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.
class CharacterTestCase(TestCase):
    
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

    def test_create_character(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        data = {
            "first_name": "Director Test First Name",
            "last_name": "Director Test Last Name",
            "description": "Test Director description."
        }
        response = client.post("/films_directors/", data, format="json")
        director = json.loads(response.content)

        data = {
            "name": "Test Planet",
            "description": "Description of Test Planet."
        }
        response = client.post("/planets/", data, format="json")
        planet = json.loads(response.content)

        data = {
            "name": "Test Production Co.",
            "description": "Description of Test Production Co."
        }
        response = client.post("/production_companies/", data, format="json")
        production_company = json.loads(response.content)
        
        data = {
            "title": "Test Film",
            "opening_text": "Opening text of Test Film...",
            "release_date": "2022-01-01",
            "director": director["id"],
            "production_companies": [production_company["id"]],
            "planets": [planet["id"]],
            "description": "Test description of Test Film."
        }
        response = client.post("/films/", data, format="json")
        film = json.loads(response.content)

        data = {
            "name": "Character Test First Name",
            "height": 1.9,
            "gender": "Test gender",
            "specie": "Test specie",
            "films": [film['id']],
            "description": "Test Character description."
        }
        response = client.post("/characters/", data, format="json")
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("height" in content.keys())
        self.assertTrue("gender" in content.keys())
        self.assertTrue("specie" in content.keys())
        self.assertTrue("films" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_read_character(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        data = {
            "first_name": "Director Test First Name",
            "last_name": "Director Test Last Name",
            "description": "Test Director description."
        }
        response = client.post("/films_directors/", data, format="json")
        director = json.loads(response.content)

        data = {
            "name": "Test Planet",
            "description": "Description of Test Planet."
        }
        response = client.post("/planets/", data, format="json")
        planet = json.loads(response.content)

        data = {
            "name": "Test Production Co.",
            "description": "Description of Test Production Co."
        }
        response = client.post("/production_companies/", data, format="json")
        production_company = json.loads(response.content)
        
        data = {
            "title": "Test Film",
            "opening_text": "Opening text of Test Film...",
            "release_date": "2022-01-01",
            "director": director["id"],
            "production_companies": [production_company["id"]],
            "planets": [planet["id"]],
            "description": "Test description of Test Film."
        }
        response = client.post("/films/", data, format="json")
        film = json.loads(response.content)

        data = {
            "name": "Character Test First Name",
            "height": 1.9,
            "gender": "Test gender",
            "specie": "Test specie",
            "films": [film['id']],
            "description": "Test Character description."
        }
        response = client.post("/characters/", data, format="json")
        content = json.loads(response.content)

        response = client.get(f"/characters/{content['id']}/")
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("height" in content.keys())
        self.assertTrue("gender" in content.keys())
        self.assertTrue("specie" in content.keys())
        self.assertTrue("films" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_update_character(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        data = {
            "first_name": "Director Test First Name",
            "last_name": "Director Test Last Name",
            "description": "Test Director description."
        }
        response = client.post("/films_directors/", data, format="json")
        director = json.loads(response.content)

        data = {
            "name": "Test Planet",
            "description": "Description of Test Planet."
        }
        response = client.post("/planets/", data, format="json")
        planet = json.loads(response.content)

        data = {
            "name": "Test Production Co.",
            "description": "Description of Test Production Co."
        }
        response = client.post("/production_companies/", data, format="json")
        production_company = json.loads(response.content)
        
        data = {
            "title": "Test Film",
            "opening_text": "Opening text of Test Film...",
            "release_date": "2022-01-01",
            "director": director["id"],
            "production_companies": [production_company["id"]],
            "planets": [planet["id"]],
            "description": "Test description of Test Film."
        }
        response = client.post("/films/", data, format="json")
        film = json.loads(response.content)

        data = {
            "name": "Character Test First Name",
            "height": 1.9,
            "gender": "Test gender",
            "specie": "Test specie",
            "films": [film['id']],
            "description": "Test Character description."
        }
        response = client.post("/characters/", data, format="json")
        content = json.loads(response.content)

        data = {
            "name": "Updated Character Test First Name",
            "height": 1.7,
            "gender": "Updated Test gender",
            "specie": "Updated Test specie",
            "films": [film['id']],
            "description": "Updated Test Character description."
        }
        response = client.put(f"/characters/{content['id']}/", data, format="json")
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("name" in content.keys())
        self.assertTrue("height" in content.keys())
        self.assertTrue("gender" in content.keys())
        self.assertTrue("specie" in content.keys())
        self.assertTrue("films" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_delete_character(self):
        client = APIClient()
        data = {"username": self.__username, "password": self.__password}
        response = client.post("/api-token-auth/", data, format="json")
        content = json.loads(response.content)
        token = content['token']
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        data = {
            "first_name": "Director Test First Name",
            "last_name": "Director Test Last Name",
            "description": "Test Director description."
        }
        response = client.post("/films_directors/", data, format="json")
        director = json.loads(response.content)

        data = {
            "name": "Test Planet",
            "description": "Description of Test Planet."
        }
        response = client.post("/planets/", data, format="json")
        planet = json.loads(response.content)

        data = {
            "name": "Test Production Co.",
            "description": "Description of Test Production Co."
        }
        response = client.post("/production_companies/", data, format="json")
        production_company = json.loads(response.content)
        
        data = {
            "title": "Test Film",
            "opening_text": "Opening text of Test Film...",
            "release_date": "2022-01-01",
            "director": director["id"],
            "production_companies": [production_company["id"]],
            "planets": [planet["id"]],
            "description": "Test description of Test Film."
        }
        response = client.post("/films/", data, format="json")
        film = json.loads(response.content)

        data = {
            "name": "Character Test First Name",
            "height": 1.9,
            "gender": "Test gender",
            "specie": "Test specie",
            "films": [film['id']],
            "description": "Test Character description."
        }
        response = client.post("/characters/", data, format="json")
        content = json.loads(response.content)

        response = client.delete(f"/characters/{content['id']}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
