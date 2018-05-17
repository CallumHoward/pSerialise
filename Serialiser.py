import abc


class Serialiser(abc.ABC):
    """
    Serialiser, abstract interface for serialisers
    """

    @staticmethod
    @abc.abstractmethod
    def serialise(data):
        """return serialised data"""
        pass


    @staticmethod
    @abc.abstractmethod
    def deserialise(serialised):
        """return deserialised data"""
        pass


    class DeserialiseError(Exception):
        def __init__(self, message):
            super().__init__(message)
