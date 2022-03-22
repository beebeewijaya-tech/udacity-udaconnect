import sys
import os

from kafka import KafkaConsumer
import logging

TOPIC_NAME = "udacitylogs"
KAFKA_SERVER = os.environ["KAFKA_SERVER"] + ':' + os.environ["KAFKA_PORT"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])
consumer.topics()


handler = logging.StreamHandler(sys.stdout)
err_handler = logging.StreamHandler(sys.stderr)
logging.basicConfig(level=logging.INFO, handlers=[handler, err_handler])

for message in consumer:
    logging.info(message)
