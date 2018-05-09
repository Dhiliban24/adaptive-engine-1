# adaptive-engine

The ALOSI adaptive engine is a web application that powers the recommendation of learning resources to learners based on real-time activity. This application is designed to be used with the [Bridge for Adaptivity](https://github.com/harvard-vpal/bridge-adaptivity), which handles the serving of activities recommended by the engine.

## Contents
This repository contains the Django web application code, and related documentation/writeups for the adaptive engine.

Folder contents:
* `app/` - Adaptive engine web application (python/django) code
* `data/` - data for engine initialization and data processing/transform scripts
* `monitoring/` - terraform files for setting up cloudwatch alarms on an elastic beanstalk deployment
* `python_prototype/` - python prototype for adaptive engine
* `r_prototype/` - R prototype for adaptive engine
* `tests/` - Testing scripts, including load testing with Locust
* `writeup/` - Writeup and LaTeX files to generate the document

## Getting started
* [Python engine library folder and documentation](https://github.com/harvard-vpal/adaptive-engine/tree/master/alosi_engine)
* [Web application folder and documentation](https://github.com/harvard-vpal/adaptive-engine/tree/master/app)
* [Theoretical overview of the recommendation engine algorithm](https://github.com/harvard-vpal/adaptive-engine/blob/master/writeup/writeup.pdf)
