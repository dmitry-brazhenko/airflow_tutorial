# Informations
* Based on [ubuntu](https://hub.docker.com/_/ubuntu) official Docker image
* This is not a production solution
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)

# Install
```shell
git clone https://github.com/dmitry-brazhenko/airflow_tutorial.git
make launch
```

# Usage
* UI link: [localhost:8080](http://localhost:8080/) (login: admin, password: admin)
* Custom python packages can be added to `requirements.txt`
* Dags are located in `dags` folder
* Connect inside docker container: `make connect`
# 