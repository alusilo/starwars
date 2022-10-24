# starwars
API for a Star Wars fan page. This API manage the information about characters, films, and planets of Star Wars movies.

## Setup

To setup this API it is necesary to install requirements as follows

```console
$ pip install -r requirements.txt
```
This will install the following Python libraries:

- django (version = 3.1)
- djangorestframework (version = 3.12)
- drf-yasg (version = 1.21.4)
- python-dotenv (version = 0.21.0)
- django-filter (version = 21.1)

After installing requirements we have to set up the system by adding a environment variable, from where is taken the secret key of the application. This is donde as follows:

```console
$ export STAR_WARS_SECRET_KEY="secret key"
```

After setting up the system we have to create tables in database:

```console
$ python manage.py makemigrations character film planet
$ python manage migrate
```

With all database created it follows to populate the database with initial data:

```console
$ python manage.py loaddata apps/planet/fixtures/initial_data.json
$ python manage.py loaddata apps/planet/film/initial_data.json
$ python manage.py loaddata apps/planet/character/initial_data.json
```

## Use cases

First of all, to start the API we have to execute the following command:

```console
$ python manage.py runserver
```

or configure a web server to manage the Django application.

The following examples are carried out using ```curl```.

To start using the API endpoints it is necessary to create a user, it can be done by executing:

```console
$ python manage.py createsuperuser
```

after executing the previous command we have to give an username, an email, and a password. Using the given user information we are going to generate access tokens to interact with API endpoints. Following are the API endpoints use cases.

### User Token endpoint

If the user ```test_user``` with password ```test_password``` needs a user token we can get a token by executing:

```console
$ curl -X POST http://127.0.0.1:8000/api-token-auth/ -H 'Content-Type: application/json' -d '{"username": "test_user", "password": "test_password"}'
```

This will return a JSON data just like:

```console
{"token":"1839a915aa0bddd0e1a4a696f95d9c6f96ac0078"}
```

### Planets endpoints

To create a planet:

```console
curl -X POST http://127.0.0.1:8000/planets/ -d '{"name": "Planet X", "description": "Planet X description"}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"name":"Planet X","description":"Planet X description"}
```

If we want to read the planet with ```id=1```:
```console
curl -X GET http://127.0.0.1:8000/planets/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

The obtained response:
```console
{"id":1,"name":"Planet X","description":"Planet X description"}
```

If we want to modify some data of planet with ```id=1```:

```console
curl -X PUT http://127.0.0.1:8000/planets/1/ -d '{"name": "Planet Y", "description": "Planet Y description"}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"name":"Planet Y","description":"Planet Y description"}
```

If we want to delete planet with ```id=1```

```console
curl -X DELETE http://127.0.0.1:8000/planets/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

### Films endpoints

To create a film we first have to have some planets created, and we also need directors and production companies created.

The directors are created as follows:

```console
curl -X POST http://127.0.0.1:8000/films_directors/ -d '{"first_name": "Director First Name", "last_name": "Director Last Name",  "description": "Director description"}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"first_name":"Director First Name","last_name":"Director Last Name","description":"Director description"}
```

And the production companies are created as follows:

```console
curl -X POST http://127.0.0.1:8000/production_companies/ -d '{"name": "Production Company", "description": "Production Company description"}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"name":"Production Company","description":"Production Company description"}
```

To create a film using a planet, a director, and a production company with ```id=1```, all of them, we proceed as follows:

```console
curl -X POST http://127.0.0.1:8000/films/ -d '{"title": "Film Title", "description": "Film description", "opening_text": "Opening text...", "release_date": "2022-01-01", "director": 1, "production_companies": [1], "planets": [1]}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"title":"Film Title","description":"Film description","opening_text":"Opening text...","release_date":"2022-01-01","director":1,"production_companies":[1],"planets":[1]}
```

If we want to read the film with ```id=1```:
```console
curl -X GET http://127.0.0.1:8000/films/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

The obtained response:
```console
{"id":1,"title":"Film Title","description":"Film description","opening_text":"Opening text...","release_date":"2022-01-01","director":1,"production_companies":[1],"planets":[1]}
```

If we want to modify some data of film with ```id=1```:

```console
curl -X PUT http://127.0.0.1:8000/films/1/ -d '{"title": "Modified film Title", "description": "Modified film description", "opening_text": "Modified opening text...", "release_date": "2022-01-01", "director": 1, "production_companies": [1], "planets": [1]}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"title":"Modified film Title","description":"Modified film description","opening_text":"Modified opening text...","release_date":"2022-01-01","director":1,"production_companies":[1],"planets":[1]}
```

If we want to delete film with ```id=1```

```console
curl -X DELETE http://127.0.0.1:8000/films/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

### Characters endpoints

To create a character we first have to have some films created. To create a character using a film with ```id=1```, we proceed as follows:

```console
curl -X POST http://127.0.0.1:8000/characters/ -d '{"name": "Character Name", "gender": "Gender", "specie": "Specie", "height": 1.8, "description": "Character description", "films": [1]}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"name":"Character Name","gender":"Gender","specie":"Specie","height":1.8,"description":"Character description","films":[1]}
```

If we want to read the film with ```id=1```:
```console
curl -X GET http://127.0.0.1:8000/characters/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

The obtained response:
```console
{"id":1,"name":"Character Name","gender":"Gender","specie":"Specie","height":1.8,"description":"Character description","films":[1]}
```

If we want to modify some data of character with ```id=1```:

```console
curl -X PUT http://127.0.0.1:8000/characters/1/ -d '{"name": "Modified Character Name", "gender": "Modified Gender", "specie": "Modified Specie", "height": 1.7, "description": "Modified Character description", "films": [1]}' -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078' -H 'Content-Type: application/json'
```

The obtained response:

```console
{"id":1,"name":"Modified Character Name","gender":"Modified Gender","specie":"Modified Specie","height":1.7,"description":"Modified Character description","films":[1]}
```

If we want to delete character with ```id=1```

```console
curl -X DELETE http://127.0.0.1:8000/characters/1/ -H 'Authorization: Token 1839a915aa0bddd0e1a4a696f95d9c6f96ac0078'
```

## Testing

To test this API there are 5 test per app. To test all the apps we have to execute the following commands:

```console
$ python manage.py test apps/planet/
$ python manage.py test apps/film/
$ python manage.py test apps/character/
```
