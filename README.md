# adaptive-engine

This repository contains the adaptive engine to be used in a Microsoft EdX course (DAT222x) in Fall 2017, along with prototypes and documentation.

## Contents
In this repo:
* `app/` - Adaptive engine web application (python/django) code
* `data/` - data for engine initialization and data processing/transform scripts
* `python_prototype/` - python prototype for adaptive engine
* `r_prototype/` - R prototype for adaptive engine
* `writeup/` - Writeup and LaTeX files to generate the document

## Running the engine application locally

You may want to set up a virtual environment / [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) beforehand.

```
# clone the repo locally
git clone https://github.com/harvard-vpal/adaptive-engine

# change into app directory
cd app
```

Run directly:
```
# install dependencies
pip install -r requirements.py

# start the app
python manage.py runserver
```

Or you can use docker:
```
docker-compose -f docker-compose_local.yaml up
```

The engine should now be available at localhost:8000

## Running tests
[Django unit tests](https://docs.djangoproject.com/en/1.11/topics/testing/overview/) in `app/tests` can be run using
```
python manage.py test
```
