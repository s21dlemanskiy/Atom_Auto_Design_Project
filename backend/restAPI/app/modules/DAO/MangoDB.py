from os import getenv, path
from dotenv import load_dotenv, find_dotenv

from logging import info, error

from pymongo import MongoClient, collection, errors

load_dotenv(find_dotenv())


class MangoDB:
    def __init__(self):
        self._collection = None
        self._session = None
        self._client = MongoClient(getenv("MONGO_HOST"), getenv("MONGO_PORT"))
        self._db = self._client[getenv("MONGO_DB")]

    def __enter__(self):
        self._session = self._client.start_session().__enter__()
        try:
            self._db.command("serverStatus")
        except errors.ServerSelectionTimeoutError as e:
            error(f"Can't access to server with {self}")
            raise ConnectionError()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self._session.__exit__()
        self._session = None
        self._client.close()

    def insert_one(self, *args, **kwargs):
        if self._session is None or self._collection is None:
            raise ValueError("Bad use of MangoDB class (session or collection is empty)"
                             " (please use it like: with MongoDB as client:..)")
        return self._collection.insert_one(*args, session=self._session, **kwargs)

    def insert_many(self, *args, **kwargs):
        if self._session is None or self._collection is None:
            raise ValueError("Bad use of MangoDB class (session or collection is empty)"
                             " (please use it like: with MongoDB as client:..)")
        return self._collection.insert_many(*args, session=self._session, **kwargs)

    def find(self, *args, **kwargs):
        if self._session is None or self._collection is None:
            raise ValueError("Bad use of MangoDB class (session or collection is empty)"
                             " (please use it like: with MongoDB as client:..)")
        return self._collection.find(*args, session=self._session, **kwargs)

    def find_one(self, *args, **kwargs):
        if self._session is None or self._collection is None:
            raise ValueError("Bad use of MangoDB class (session or collection is empty)"
                             " (please use it like: with MongoDB as client:..)")
        return self._collection.find_one(*args, session=self._session, **kwargs)

    def update_one(self, *args, **kwargs):
        if self._session is None or self._collection is None:
            raise ValueError("Bad use of MangoDB class (session or collection is empty)"
                             " (please use it like: with MongoDB as client:..)")
        return self._collection.update_one(*args, session=self._session, **kwargs)

    def abort_transaction(self):
        if self._session is None:
            raise ValueError("Bad use of MangoDB class (session is empty)"
                             " (please use it like: with MongoDB as client:..)")
        self._session.abort_transaction()


    def get_collection(self, collection: str) -> collection.Collection:
        self._collection = self._db[collection]

    def __str__(self):
        return f"{self.__class__.__name__}[client={self._client}, DB={self._db}]"

    def __repr__(self):
        return self.__str__()