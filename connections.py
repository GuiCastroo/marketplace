import os
from sqlalchemy import create_engine, MetaData, Table


class Connections:
    @staticmethod
    def get_env_variable(name):
        try:
            return os.environ[name]
        except KeyError:
            message = f"Expected environment variable '{name}' not set."
            raise Exception(message)

    @classmethod
    def url(cls):
        postgres_url = cls.get_env_variable("POSTGRES_URL")
        postgres_user = cls.get_env_variable("POSTGRES_USER")
        postgres_pw = cls.get_env_variable("POSTGRES_PW")
        postgres_db = cls.get_env_variable("POSTGRES_DB")
        return f'postgresql+psycopg2://{postgres_user}:{postgres_pw}@{postgres_url}/{postgres_db}'

    def __init__(self, table_name):
        self.__engine = create_engine(self.url(), convert_unicode=True)
        self.__meta_data = MetaData(bind=self.__engine)
        self._table_name = Table(table_name, self.__meta_data, autoload=True)

    @property
    def table(self):
        return self._table_name

    @table.setter
    def table(self, new_table):
        self._table_name = new_table

    def connect(self):
        connect = self.__engine.connect()
        return connect
