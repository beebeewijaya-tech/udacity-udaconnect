import os
from google.protobuf.json_format import MessageToDict
import psycopg2

import grpc

from proto import location_pb2, location_pb2_grpc
from concurrent import futures

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

connection = psycopg2.connect(user=DB_USERNAME,
                                  password=DB_PASSWORD,
                                  host=DB_HOST,
                                  port=DB_PORT,
                                  database=DB_NAME)

class LocationServices(location_pb2_grpc.LocationServiceServicer):
    def GetLocation(self, request, context):
        dict_obj = MessageToDict(request)
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from location where id = %s"

        cursor.execute(postgreSQL_select_Query, dict_obj['id'])
        cursor.fetchall()

        return request


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServices(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()
