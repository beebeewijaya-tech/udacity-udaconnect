from proto import log_pb2, log_pb2_grpc
import grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = log_pb2_grpc.LogServiceStub(channel)

    req = log_pb2.LogMessage(
        message="Test Log",
        level="INFO"
    )

    resp = stub.SendLog(req)
    print(resp)

run()