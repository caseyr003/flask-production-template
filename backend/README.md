# Flask API Template

This project is a web app built with Python and Flask to be used as a starter template.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Python 3](https://www.python.org/)
* [Docker](https://www.docker.com/)

## Installation

* run `git clone https://github.com/caseyr003/flask-production-template.git`

## Running

To run the project locally follow the following steps:

* change into the project directory
* uncomment last line in `Dockerfile`
* `docker build -t api .`
* `docker run -p 5000:5000 api`

## JSON API

The JSON API is a test endpoint to start development

* `http://localhost:5000/api/test`
(returns a test json response)

## License

This project is licensed under the MIT License
