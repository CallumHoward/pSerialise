import json
from Serialiser import Serialiser


class JsonSerialiser(Serialiser):
    """
    JsonSerialiser, json implementation of Serialiser
    """

    @staticmethod
    def serialise(data):
        return json.dumps(data.__dict__, indent=4)


    @staticmethod
    def deserialise(serialised, dataContainer):
        #TODO exception handling
        data = json.loads(serialised)  # loads as a dictionary
        return dataContainer(**data)  # expand into keyword arguments
