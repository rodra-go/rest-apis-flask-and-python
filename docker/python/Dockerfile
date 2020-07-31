FROM ubuntu:18.04

# bring system up-to-date
RUN apt-get update -q && \
apt-get upgrade -qy

# install python
RUN apt-get install -y build-essential python3.8 python3.8-dev python3-pip python3.8-venv sudo nano

# update pip
RUN python3.8 -m pip install pip --upgrade
RUN python3.8 -m pip install wheel

# create a non-root user
RUN useradd -p $(openssl passwd -1 '') docker
RUN usermod -aG sudo docker
RUN usermod -aG 100 docker

# Install python libraries
RUN pip install Flask-RESTful
RUN pip install Flask-JWT
RUN pip install Flask-SQLAlchemy

EXPOSE 5000

USER docker
