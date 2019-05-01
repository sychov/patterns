#-----------------------------------------------------------------------------#
# Name:         adapter.py
# Author:       Ryoga
# Created:      29.04.2019
# Description:  Adapter pattern demo.
#               Aim: make possibility to work with a class, that has
#               incompartible interface.
#-----------------------------------------------------------------------------#


import abc
import json
from typing import List


# -------------------- INTERFACE ------------------------- #

class Serializer(abc.ABC):
    """Abstract Serializer class.
    Just for demonstration.
    """
    @abc.abstractmethod
    def serialize(self, data) -> str:
        """Serialize something to string.
        """
        pass

    @abc.abstractmethod
    def deserialize(self, data: str):
        """Deserialize something from string.
        """
        pass


# -------------------- BASIC IMPLEMENTATION ------------------------- #


class Client:
    """Client demo.
    """
    def __init__(self, serializer: Serializer):
        self._serializer = serializer

    def run(self, test_data):
        print('"%s" testing:' % self._serializer.__class__.__name__)
        print('   - serialize:')
        serialized_data = self._serializer.serialize(test_data)
        print('       %s --> "%s"' % (str(test_data), serialized_data))
        print('   - deserialize:')
        deserialized_data = self._serializer.deserialize(serialized_data)
        print('       "%s" --> %s' % (serialized_data, str(deserialized_data)))


class StringsListSerializer(Serializer):
    """Particular Serializer class for lists of strings.
    Just for demonstration.
    """
    SEPARATOR = '/\\'
    def serialize(self, strings_list: List[str]) -> str:
        return self.SEPARATOR.join(strings_list)

    def deserialize(self, data: str) -> List[str]:
        return data.split(self.SEPARATOR)


# ----------------- JSON ADAPTER IMPLEMENTATION ---------------------- #

class JsonSerializer(Serializer):
    """Adapter between JSON library used Serializer class.
    """
    def serialize(self, data) -> str:
        return json.dumps(data)

    def deserialize(self, data: str):
        return json.loads(data)


# --------------------------- TEST --------------------------------

if __name__ == '__main__':
    test_data = ['one', 'two', 'three']
    string_list_client = Client(StringsListSerializer())
    string_list_client.run(test_data)
    json_client = Client(JsonSerializer())
    json_client.run(test_data)


