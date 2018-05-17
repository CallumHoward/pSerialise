import pickle
from Serialiser import Serialiser


class PickleSerialiser(Serialiser):
    """
    PickleSerialiser, Pickle implementation of Serialiser
    """

    @staticmethod
    def serialise(data):
        serialised = pickle.dumps(data)

        return serialised


    @staticmethod
    def deserialise(serialised, dataContainer):
        try:
            data = pickle.loads(serialised)  # load as a list of dictionaries

        except:
            raise Serialiser.DeserialiseError(
                    "Failed to restore python object. Could not deserialise target data")

        return data
