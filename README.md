# docker_flask_homework
HHA504 / Cloud Computing / Assignment 8 / Docker

This repo aims to provide hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple applications.

# Documentation 

1. [Dockerizing a Single Flask Application](#1-dockerizing-a-single-flask-application)
2. [Multi-Container Setup with Docker Compose](#2-multi-container-setup-with-docker-compose)

### 1. Dockerizing a Single Flask Application
In Part 1 of the assignment, located in the folder labeled **Part1**, I dockerized a simple Flask application with the following steps: 
1. Created a script for the flask application in a python file (**app.py**) with relevant html files in the templates folder.
2. Created a **requirements.txt** file that contains ```flask```. 
3. Created a file called **Dockerfile** with the following code:
```
 # Sets a pre-built package/base image for the Docker image
FROM python:3.7-alpine  
# Creates a new folder called 'app' and makes it the working directory inside the container
WORKDIR /app
# Copies everything on the current directory onto the 'app' directory inside the container
COPY . /app
# Installs the Python dependencies listed in the requirements.txt file.
RUN pip install -r requirements.txt 
# Exposes port 5000 to the operating system and informs Docker that the container will listen on port 5000 at runtime 
EXPOSE 5000
# Specifies the command that will be executed when the container starts
CMD ["python", "app.py"]
```
4. After created the app.py file, Dockerfile, and requirements.txt file, the Flask application is ready to be dockerized.
     + First, in the terminal, build the image by running: ```docker build -t <image name> .``` Use ```docker images``` to view the creates docker image(s). 
     + To run the docker container after the image is built, run : ```3. docker run -p 5000:5000 <image name>```. The ```-p 5000:5000``` part of the command maps port 5000 on the host to port 5000 on the container and can be changed to open in any port (```-p <port #>:5000```.
     + The command ```docker run -d p 5000:5000 <image name>``` can be used to run the docker container in a detached mode. ```docker ps``` gets a list of the current running containers and can be used to view the docker containers running in detached mode. To stop the running docker containers, ```docker stop  <container id>``` can be used, with ```<container id>``` taken from ```docker ps```.
5. If updates or changes were made to the Flask scripts, the docker image need to be rebuilt and the docker container rerun with the respective commands. 

### 2. Multi-Container Setup with Docker Compose
In Part 2 of the assignment, located in the folder labeled **Part2**, I dockerized 2 simple Flask applications with Docker Compose using the following steps.  Docker Compose allows for creation of multiple docker services, each with its own configuration, dependencies, and container definitions. 
1. Created two folders, each containing the script for the Flask application, a requirements.txt file, and a Dockerfile. The Dockerfile contains the relevant script explained above.
2. Created a file called `docker-compose.yaml` containing the following:
```
version: '3'             # specifies the version of the Docker Compose file syntax being used.
services:
  flask_app_1:           # specifies the name of the service
    build: ./flask1      # specifies the local directory/folder of the Dockerfile 
    ports:
      - "5001:5000"
    volumes:
      - ./flask1:/app    # maps the local directory ./flask1 into the /app directory inside the container
  flask_app_2:           
    build: ./flask2      
    ports:
      - "5002:5000"
    volumes:
      - ./flask2:/app
```
3. To build and run the services in the `docker-compose.yaml` file, run: ```docker-compose up --build```.
4. ```docker-compose up -d``` can be used to run the services on the background. ```docker-compose ps``` gets a list of the current running services, and ```docker-compose down``` stops the docker services. 


