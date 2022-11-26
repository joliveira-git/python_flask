class Config:
    TESTING = False
    SECRET_KEY = "supersecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///mypet.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///mypet_test.sqlite"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///mypet.sqlite"
