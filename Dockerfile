FROM ubuntu:latest

MAINTAINER Vladimir Melnikov "admin@csgo-boost.ru"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3
	
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5050

ENTRYPOINT [ "python3" ]

CMD [ "primefactor.py" ]