# co2tracker-api

[![Build Status](https://travis-ci.org/migomi3/co2tracker-api.svg?branch=master)](https://travis-ci.org/migomi3/co2tracker-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Co2Tracker for hackathon.. Check out the project's [documentation](http://migomi3.github.io/co2tracker-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
