### Intro

This project uses [Uvicorn](https://www.uvicorn.org/) and [FasAPI](https://fastapi.tiangolo.com/) to connect to a local instance of Redis.

Redis is an open source (BSD licensed), in-memory data structure store, used as a database.

Uvicorn is an ASGI web server implementation for Python.

### Requirements
To run the project you need Python 3.10 and Docker.
Run the following commands:

`pip install pipenv`

`pipenv shell`

`pipenv install`

`pipenv --venv` - to see which environment are you using then select that virtual env (perhaps from IDE interface)

### Run the server

`uvicorn main:app --reload`

The server communicates with a local Redis running in a docker container. To pull the redis docker image and then start the container do:

`docker pull redis`

`docker run -p 6379:6379 redis`

### Access the redis CLI 
Install redis-cli:

`sudo apt update`

`sudo apt install redis-tools`


Access redis-cli

`redis-cli`

Here you can set, get or delete key value pairs:
- set `set KEY VALUE`
- get `get KEY`
- delete `delete KEY`
