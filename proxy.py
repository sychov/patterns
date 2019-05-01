#-----------------------------------------------------------------------------#
# Name:         proxy.py
# Author:       Ryoga
# Created:      26.04.2019
# Description:  Proxy class pattern.
#               Main idea: to wrap target class instance ("component")
#               with class that uses the same interface and CHANGE some
#               logics of it's methods.
#-----------------------------------------------------------------------------#

import abc
import time


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


# ------------------ IMPLEMENTATION ----------------------- #

class RemoteStorage(Storage):
    """Storage class, that stores data in memory.
    Just imageine, that it operate data not in memory... but
    somewhere far far away!
    """
    def __init__(self):
        self._storage = {}

    def put(self, key: str, data: str):
        print(' - put "%s" data to remote torage.' % key)
        self._storage[key] = data

    def get(self, key: str) -> str:
        print(' - get "%s" key from remote storage.' % key)
        return self._storage.get(key)


class ProxyStorage(Storage):
    """Logging decorator class, for Storage class.
    Log to console when put() and get() methods are called.
    """
    TIMEDELTA = 5

    def __init__(self, target_storage: Storage):
        self._target_storage = target_storage
        self._cache = {}

    def put(self, key: str, data: str):
        return self._target_storage.put(key, data)

    def get(self, key: str) -> str:
        if (key in self._cache and
                    time.time() - self._cache[key]['time'] < self.TIMEDELTA):
            print(' - get "%s" key from cache.' % key)
            return self._cache[key]['data']
        else:
            data = self._target_storage.get(key)
            self._cache[key] = {'data': data, 'time': int(time.time())}
            print(' - cached "%s"' % key)
            return data


# ------------------------- TEST --------------------------- #

if __name__ == '__main__':
    print('Memory storage logging test:')
    storage = RemoteStorage()
    proxy = ProxyStorage(storage)
    proxy.put('some_key', 'some_value')
    for _ in range(5):
        proxy.get('some_key')

