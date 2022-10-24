import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.
class FilmTestCase(TestCase):
    
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

    def test_create_film(self):
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
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("title" in content.keys())
        self.assertTrue("opening_text" in content.keys())
        self.assertTrue("release_date" in content.keys())
        self.assertTrue("director" in content.keys())
        self.assertTrue("planets" in content.keys())
        self.assertTrue("production_companies" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_read_film(self):
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
        content = json.loads(response.content)

        response = client.get(f"/films/{content['id']}/")
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("title" in content.keys())
        self.assertTrue("opening_text" in content.keys())
        self.assertTrue("release_date" in content.keys())
        self.assertTrue("director" in content.keys())
        self.assertTrue("planets" in content.keys())
        self.assertTrue("production_companies" in content.keys())
        self.assertTrue("description" in content.keys())
    
    def test_update_film(self):
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
        content = json.loads(response.content)

        data = {
            "title": "Modified Test Film",
            "opening_text": "Modified Opening text of Test Film...",
            "release_date": "2022-01-02",
            "director": director["id"],
            "production_companies": [production_company["id"]],
            "planets": [planet["id"]],
            "description": "Modified Test description of Test Film."
        }
        response = client.put(f"/films/{content['id']}/", data, format="json")
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in content.keys())
        self.assertTrue("title" in content.keys())
        self.assertTrue("opening_text" in content.keys())
        self.assertTrue("release_date" in content.keys())
        self.assertTrue("director" in content.keys())
        self.assertTrue("planets" in content.keys())
        self.assertTrue("production_companies" in content.keys())
        self.assertTrue("description" in content.keys())

    def test_delete_film(self):
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
        content = json.loads(response.content)

        response = client.delete(f"/films/{content['id']}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        