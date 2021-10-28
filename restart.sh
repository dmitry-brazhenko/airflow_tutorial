docker rm -f $(docker ps | grep airflow | awk '{print $1}')
docker build -t airflow .
docker run -it -p 8080:8080 --mount type=bind,source="$(pwd)"/dags,target=/root/airflow/dags   -v /var/run/docker.sock:/var/run/docker.sock airflow