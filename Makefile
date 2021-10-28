current_dir = $(shell pwd)

stop:
		(docker container ls -a | grep airflow_tutorial | awk '{print $$1}')  | xargs -r docker container stop

remove:
		(docker container ls -a | grep airflow_tutorial | awk '{print $$1}')  | xargs -r docker rm

build:
		docker build -t airflow_tutorial .

run:
		docker run -it -p 8080:8080 --mount type=bind,source="$(current_dir)"/dags,target=/root/airflow/dags   -v /var/run/docker.sock:/var/run/docker.sock airflow_tutorial

launch:
		make stop
		make remove
		make build
		make run

connect:
		container_id="$(shell (docker ps| grep airflow| awk '{print $$14}') )";docker exec -it $$container_id /bin/zsh
