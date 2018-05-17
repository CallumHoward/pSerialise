import json
from Serialiser import Serialiser


class JsonSerialiser(Serialiser):
    """
    JsonSerialiser, json implementation of Serialiser
    """

    @staticmethod
    def serialise(data):
        try:
            serialised = json.dumps([element.__dict__ for element in data], indent=4)

        except TypeError:
            raise

        except:
            raise

        return serialised


    @staticmethod
    def deserialise(serialised, dataContainer):
        try:
            raw_data = json.loads(serialised)  # load as a list of dictionaries
            data = [dataContainer(**element) for element in raw_data]

        except json.decoder.JSONDecodeError:
            raise Serialiser.DeserialiseError(
                    "Failed to decode JSON. Could not deserialise target data")

        except TypeError:
            raise Serialiser.DeserialiseError(
                    "Failed to restore python object. Could not deserialise target data")

        except:  # propagate unexpected exceptions
            raise

        return data
