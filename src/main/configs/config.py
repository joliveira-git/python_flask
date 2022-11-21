class Config:
    TESTING = False
    SECRET_KEY = "supersecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///storage.db"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///storage_test.db"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///storage.db"
