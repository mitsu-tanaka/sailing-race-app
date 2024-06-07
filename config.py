class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'your-secret-key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/tanakamitsuru/sailing-race-app.db'
