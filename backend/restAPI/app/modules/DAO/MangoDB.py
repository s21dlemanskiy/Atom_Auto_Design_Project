from os import getenv
from dotenv import load_dotenv, find_dotenv

from logging import info, error

from pymongo import MongoClient, collection, errors

load_dotenv()


class MangoDB:
    is_transaction_allow = False
    def __init__(self):
        self._collection = None
        self._session = None
        # транзакции работают только на кластере MangoDB
        # но не работают на stand-alone сервере без щардирования и резервно копирования
        self.__class__.is_transaction_allow = getenv("ALLOW_MANGO_TRANSACTION", False)
        #
        self._client = MongoClient(getenv("MONGO_HOST"), int(getenv("MONGO_PORT")))
        self._db = self._client[getenv("MONGO_DB")]

    def __enter__(self):
        self._session = self._client.start_session().__enter__()
        if self.__class__.is_transaction_allow:
            self._transaction = self._session.start_transaction().__enter__()
        try:
            self._db.command("serverStatus")
        except errors.ServerSelectionTimeoutError as e:
            error(f"Can't access to server with {self}")
            raise ConnectionError()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__class__.is_transaction_allow:
            self._transaction.__exit__(exc_type, exc_val, exc_tb)
        self._session.__exit__(exc_type, exc_val, exc_tb)
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
        if not self.__class__.is_transaction_allow:
            errors("Can't abort transaction due to transaction not allowed")
            return
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