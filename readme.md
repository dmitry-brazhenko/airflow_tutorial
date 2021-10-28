# Informations
* Based on [ubuntu](https://hub.docker.com/_/ubuntu) official image
* This is not a production solution
* 

# Install

``` shell
docker rm -f $(docker ps | grep airflow | awk '{print $1}')
docker build -t airflow .
docker run -it -p 8080:8080 airflow
```

# Connect to docker container
``` shell
docker exec -it $(docker ps | grep airflow | awk '{print $14}') /bin/zsh     
```