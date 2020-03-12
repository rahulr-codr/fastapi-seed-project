# fastapi_sqlalchemy_alembic

This repo is used as a part of a tutorial to show how to use Fastapi and pydantic with Sqlalchemy, postgresql, Alembic(for migrations).

A chunk of this code has been taken from the below article. Give that man a thumbs up.

The full article is published on medium [here](https://medium.com/@ahmed.nafies/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)

## How to build

    docker-compose build

## How to run db

    docker-compose up

## Run Migrations

    alembic revision --autogenerate -m "first commmit"

    alembic upgrade head

## Run API

    uvicorn sql_app.main:app --host 0.0.0.0 --port 8000

## Documentation

    swagger - http://localhost:8000/docs
    redoc - http://localhost:8000/redoc

## Pgadmin4

    http://localhost:5050
