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
        try:
            raw_data = json.loads(serialised)  # loads as a dictionary
            data = dataContainer(**raw_data)  # expand into keyword arguments

        except json.decoder.JSONDecodeError:
            raise Serialiser.DeserialiseError(
                    "Failed to decode JSON. Could not deserialise target data")

        except TypeError:
            raise Serialiser.DeserialiseError(
                    "Failed to restore python object. Could not deserialise target data")

        except:  # propagate unexpected exceptions
            raise

        return data
