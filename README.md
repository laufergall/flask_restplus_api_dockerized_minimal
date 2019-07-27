## Purpose

This repo contains a minimal working example of a dockerized Flask-restplus API. It is meant to be used as a starting point for developing backend APIs.

## Get started

1. Clone the repository

2. Make sure you have docker installed

3. Build the docker image: 

```bash
docker build -t minimal_flask-restplus .
```

4. Run the image:

```bash
docker run -p 8399:8399 minimal_flask-restplus:latest
```

where 8399 is the port to be exposed, in this case.

5. Access the Swagger UI to interact with the PI endpoints under `http://localhost:8399/`, or `http://< docker-machine ip >:8399/` if you have the Docker Toolbox on Windows.

