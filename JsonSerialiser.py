import json
from Serialiser import Serialiser


class JsonSerialiser(Serialiser):
    """
    JsonSerialiser, json implementation of Serialiser
    """

    @staticmethod
    def serialise(data):
        return json.dumps(data.__dict__)


    @staticmethod
    def deserialise(serialised, dataContainer):
        return json.loads(serialised, cls=dataContainer)
