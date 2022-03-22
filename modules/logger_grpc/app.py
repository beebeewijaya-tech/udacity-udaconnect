import os
from google.protobuf.json_format import MessageToDict

import grpc
from kafka import KafkaProducer

from proto import log_pb2, log_pb2_grpc
from concurrent import futures

TOPIC_NAME = "udacitylogs"
KAFKA_SERVER = os.environ["KAFKA_SERVER"] + ':' + os.environ["KAFKA_PORT"]
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class LogServices(log_pb2_grpc.LogServiceServicer):
    def SendLog(self, request, context):
        dict_obj = MessageToDict(request)
        d_message = f"{dict_obj['level']}: {dict_obj['message']}".encode()
        producer.send(TOPIC_NAME, d_message)
        return request

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_pb2_grpc.add_LogServiceServicer_to_server(LogServices(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


print('MAIN')
main()
print('END')
