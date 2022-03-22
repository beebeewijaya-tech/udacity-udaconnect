from proto import location_pb2, location_pb2_grpc
import grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = location_pb2_grpc.LocationServiceStub(channel)

    req = location_pb2.LocationDetailRequest(id="30")
    resp = stub.GetLocation(req)
    print(resp)

run()