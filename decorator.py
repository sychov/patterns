#-----------------------------------------------------------------------------#
# Name:         decorator.py
# Author:       Ryoga
# Created:      23.04.2019
# Description:  Decorator class pattern.
#               Main idea: to wrap target class instance ("component")
#               with class that uses the same interface and add some
#               extra logics to it's methods.
#-----------------------------------------------------------------------------#

import abc


# -------------------- INTERFACES ------------------------- #

class Storage(abc.ABC):
    """Interface for Storage class.
    """
    @abc.abstractmethod
    def put(self, key: str, data: str):
        """Put data to storage, using key,
        """
        pass

    @abc.abstractmethod
    def get(self, key: str) -> str:
        """Get data by key from storage,
        """
        pass

class StorageDecorator(Storage):
    """Abstract Storage Decorator class.
    """
    def __init__(self, component: Storage):
        """Init decorator, set component's value.
        """
        self._component = component

# ------------------ IMPLEMENTATION ----------------------- #

class MemoryStorage(Storage):
    """Storage class, that stores data in memory.
    """
    def __init__(self):
        self._storage = {}

    def put(self, key: str, data: str):
        self._storage[key] = data

    def get(self, key: str) -> str:
        return self._storage.get(key)


class StorageLoggerDecorator(StorageDecorator):
    """Logging decorator class, for Storage class.
    Log to console when put() and get() methods are called.
    """
    def put(self, key: str, data: str):
        print(' - put "%s:%s"' % (key, data))
        return self._component.put(key, data)

    def get(self, key: str) -> str:
        data = self._component.get(key)
        print(' - get "%s" key ("%s" data)' % (key, data))
        return data


class StoragePrefixDecorator(StorageDecorator):
    """Content enchncing decorator class, for Storage class.
    Adds some prefix when string is gotten from Storage.
    Just for demo.
    """
    PREFIX = 'prefix@'

    def get(self, key: str) -> str:
        return self.PREFIX + self._component.get(key)

    def put(self, key: str, data: str):
        data = self._remove_prefix(data)
        return self._component.put(key, data)

    @classmethod
    def _remove_prefix(cls, data: str):
        if data.startswith(cls.PREFIX):
            return data.split('@', 1)[1]
        else:
            return data

# ------------------------- TEST --------------------------- #

if __name__ == '__main__':
    print('Memory storage logging test:')
    storage = MemoryStorage()
    decorator = StorageLoggerDecorator(storage)
    decorator = StoragePrefixDecorator(decorator)
    decorator.put('some_key', 'some_value')
    print('Got:', decorator.get('some_key'))

