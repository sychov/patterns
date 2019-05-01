#-----------------------------------------------------------------------------#
# Name:        abstract_factory.py
# Author:      Ryoga
# Created:     21.04.2019
# Description: Abstract factory pattern. Method to organaize
#              business logics that work with sets of items.
#-----------------------------------------------------------------------------#


import abc


# -------------------- INTERFACES ------------------------- #

class CloudStorage(abc.ABC):
    """Abstract cloud Storage.
    Declares methods:
        - get_file(),
        - put_file(),
        - delete_file()
    """
    @abc.abstractmethod
    def get_file(self, filename):
        pass

    @abc.abstractmethod
    def put_file(self, file_, filename):
        pass

    @abc.abstractmethod
    def delete_file(self, filename):
        pass


class CloudDB(abc.ABC):
    """Abstract cloud DB.
    Declares methods:
        - exec_sql(),
    """
    @abc.abstractmethod
    def exec_sql(self, sql):
        pass


class CloudQueue(abc.ABC):
    """Abstract computing Queue.
    Declares methods:
        - get_message(),
        - put_message(),
    """
    @abc.abstractmethod
    def get_message(self):
        pass

    @abc.abstractmethod
    def put_message(self, message):
        pass


class CloudServicesFactory(abc.ABC):
    """Abstract computing cloud interface class.
    Declares methods:
        - get_storage(),
        - get_db_connection(),
        - get_message_queue()
    """
    @abc.abstractmethod
    def get_storage(self, name) -> CloudStorage:
        pass

    @abc.abstractmethod
    def get_db_connection(self, name) -> CloudDB:
        pass

    @abc.abstractmethod
    def get_message_queue(self, name) -> CloudQueue:
        pass


# -------------------- AWS FACTORY ------------------------- #

class AmazonS3(CloudStorage):
    """AWS / Storage.
    """
    def get_file(self, filename):
        print('Got file from Amazon S3')

    def put_file(self, file_, filename):
        print('Put file to Amazon S3')

    def delete_file(self, filename):
        print('Deleted file from Amazon S3')


class AmazonRDS(CloudDB):
    """AWS / DB
    """
    def exec_sql(self, sql):
        print('Executed SQL in Amazon RDS')


class AmazonSQS(CloudQueue):
    """AWS / Queue
    """
    def get_message(self):
        print('Check message in Amazon SQS')

    def put_message(self, message):
        print('Put message to Amazon SQS')


class AmazonWebServicesFactory(CloudServicesFactory):
    """AWS - Factory
    """
    def get_storage(self, name) -> AmazonS3:
        return AmazonS3()

    def get_db_connection(self, name) -> AmazonRDS:
        return AmazonRDS()

    def get_message_queue(self, name) -> AmazonSQS:
        return AmazonSQS()


# -------------------- GC FACTORY ------------------------- #

class GCStorage(CloudStorage):
    """GC / Storage
    """
    def get_file(self, filename):
        print('Got file from Google Cloud Storage')

    def put_file(self, file_, filename):
        print('Put file to Google Cloud Storage')

    def delete_file(self, filename):
        print('Deleted file from Google Cloud Storage')


class GCSQL(CloudDB):
    """GC / DB
    """
    def exec_sql(self, sql):
        print('Executed SQL in Google Cloud SQL')


class GCPubSub(CloudQueue):
    """GC / Queue
    """
    def get_message(self):
        print('Check message in Google Cloud PubSub')

    def put_message(self, message):
        print('Put message to Google Cloud PubSub')


class GoogleCloudFactory(CloudServicesFactory):
    """GC - Factory
    """
    def get_storage(self, name) -> GCStorage:
        return GCStorage()

    def get_db_connection(self, name) -> GCSQL:
        return GCSQL()

    def get_message_queue(self, name) -> GCPubSub:
        return GCPubSub()


# -------------------- APPLICATION ------------------------- #

class Application:
    """Pattern's client class.
    """
    def __init__(self, cloud_services: CloudServicesFactory):
        self._storage = cloud_services.get_storage('storage_name')
        self._db = cloud_services.get_db_connection('db_name')
        self._queue = cloud_services.get_message_queue('queue_name')

    def proceed(self):
        self._queue.get_message()
        self._storage.get_file('name')
        self._storage.delete_file('name')
        self._db.exec_sql('sql')
        self._storage.put_file(b'content', 'name')
        self._queue.put_message('msg')


if __name__ == '__main__':
    print('\n~ AWS ~\n')
    aws = AmazonWebServicesFactory()
    test_app_1 = Application(aws)
    test_app_1.proceed()
    print('\n~ GC ~\n')
    gc = GoogleCloudFactory()
    test_app_2 = Application(gc)
    test_app_2.proceed()


