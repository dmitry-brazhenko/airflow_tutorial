stop:
		docker rm -f $(docker ps | grep airflow_tutorial | awk '{print $1}')

build:
		docker build -t airflow_tutorial .

run:
		docker run -it -p 8080:8080 --mount type=bind,source="$(pwd)"/dags,target=/root/airflow/dags   -v /var/run/docker.sock:/var/run/docker.sock airflow_tutorial

launch:
		make build
		make run

connect:
		docker exec -it $(docker ps | grep airflow | awk '{print $14}') /bin/zsh
