FROM python:3.8

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV PYTHONUNBUFFERED=0

COPY . .

CMD ["python3", "-u", "app.py"]
