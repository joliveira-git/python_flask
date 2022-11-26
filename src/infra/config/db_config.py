from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.configs.config import DevelopmentConfig


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self, connection_string=DevelopmentConfig.SQLALCHEMY_DATABASE_URI):
        self.__connection_string = connection_string
        self.session = None

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - engine connection to database
        """
        engine = create_engine(self.__connection_string)
        return engine

    # implementação do context manager
    def __enter__(self):
        # aqui o contexto (estado definido no __init__) é aberto para o gerenciador de contexto
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
