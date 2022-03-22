FROM ubuntu:latest

WORKDIR .


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3-pip gcc musl-dev libc-dev postgresql postgresql-client g++
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libgeos-dev libpq-dev python3-dev

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]