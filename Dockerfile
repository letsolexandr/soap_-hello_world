FROM python:3.8


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/apps/soap_service



RUN mkdir -p /opt/apps/soap_service

# copy project install
COPY ./requirements.txt /install/requirements.txt

COPY ./trembita_hello_world /opt/apps/soap_service
# install python depends
RUN pip install --upgrade pip
RUN pip install -r /install/requirements.txt


RUN chmod +x /opt/apps/soap_service/entrypoint.sh

