#-----------------------------------------------------------------------------#
# Name:         facade.py
# Author:       Ryoga
# Created:      28.04.2019
# Description:  Facade pattern demo.
#               Simple interface to a comlex system.
#-----------------------------------------------------------------------------#


from enum import Enum


class RemoteStorage:
    """Complex class for remote storage operations. Only for demonstration.
    With connections, disconnections, inner classes etc.
    Agile, but difficult to use.
    """
    class State(Enum):
        AVAILABLE = 1
        TEMPORARY_NOT_AVAILABLE = 2
        NOT_EXISTS = 3

    class Connection:
        """Storage connection object.
        """
        def __init__(self, address):
            """Storing in memory - just for testing.
            """
            self._storage = {}
            print(' - connected to "%s".' % address)

        def put(self, key: str, data: str):
            """Storing in memory - just for testing.
            """
            print(' - put "%s" data to remote torage.' % key)
            self._storage[key] = data

        def get(self, key: str) -> str:
            """Get from memory - just for testing.
            """
            print(' - get "%s" from remote storage.' % key)
            return self._storage.get(key)

        def close(self) -> str:
            """Disconnect from remote storage.
            """
            print(' - disconnected.')

    def __init__(self):
        self._connections_pool = {}

    def connect(self, address) -> 'RemoteStorage.Connection':
        """connect to storage.
        """
        if address in self._connections_pool:
            return self._connections_pool[address]
        else:
            return RemoteStorage.Connection(address)

    def check(self, address) -> State:
        """Check remote storage state.
        """
        print(' - checks <%s> availability: AVAILABLE.' % address)
        return RemoteStorage.State.AVAILABLE


class RemoteStorageFacade:
    """Simple facade for class RemoteStorage. Can be used in 95% situations.
    Only constructor, put() and get() methods.
    """
    class NotAvailableError(Exception):
        pass

    def __init__(self, address):
        self._remote_storage = RemoteStorage()
        self._address = address

    def put(self, key: str, data: str):
        self._check_remote_storage()
        connection = self._remote_storage.connect(self._address)
        connection.put('key', 'vaue')
        connection.close()

    def get(self, key: str) -> str:
        self._check_remote_storage()
        connection = self._remote_storage.connect(self._address)
        result = connection.get('key')
        connection.close()
        return result

    def _check_remote_storage(self):
        state = self._remote_storage.check(self._address)
        if state != RemoteStorage.State.AVAILABLE:
            raise self.NotAvailableError



# --------------------------- TEST --------------------------------

if __name__ == '__main__':
    rs = RemoteStorageFacade('far/far/away')
    rs.put('some_key', 'some_value')
    rs.get('some_key')


