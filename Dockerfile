# https://hub.docker.com/_/python
FROM python:3.9-slim

#Para verificar os logs no Cloud Run
ENV PYTHONUNBUFFERED True

# Instalar dependências
RUN pip install Flask==1.1.2 gunicorn==20.0.4 google-cloud-bigquery

#Copiar a imagem local para o Docker
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY *.py ./

# Run the web service on container startup. 
# Use gunicorn webserver with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
# [END eventarc_gcs_dockerfile]
