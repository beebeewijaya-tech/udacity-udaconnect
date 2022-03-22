import os
from typing import Dict, List

from app import db
from app.udaconnect.models import Person

from proto import log_pb2, log_pb2_grpc
import grpc
KAFKA_SERVER = os.environ["GRPC_SERVER"] + ':' + os.environ["GRPC_PORT"]

def run(message, level):
    channel = grpc.insecure_channel(KAFKA_SERVER)
    stub = log_pb2_grpc.LogServiceStub(channel)

    req = log_pb2.LogMessage(
        message=message,
        level=level
    )

    resp = stub.SendLog(req)
    return resp


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()
        run(f"Log Create {new_person.first_name}", "INFO")
        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        run(f"Log Retrieve {person_id}", "INFO")
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        resp = run("Log Retrieve All Person", "INFO")
        print(resp)
        return db.session.query(Person).all()
