# NGINX Template

NGINX server to deploy Flask API with Docker used as a starter template.

## Built With

* [NGINX](https://www.nginx.com/)
* [Docker](https://www.docker.com/)

## Installation

* run `git clone https://github.com/caseyr003/flask-production-template.git`

## Running

To run the project locally follow the following steps:

* change into the project directory
* `docker build -t nginx-server .`
* `docker run -p 8001:8001 nginx-server`

## License

This project is licensed under the MIT License
