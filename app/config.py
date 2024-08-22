import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
    SHOPIFY_API_PASSWORD = os.getenv('SHOPIFY_API_PASSWORD')
    SHOPIFY_STORE_NAME = os.getenv('SHOPIFY_STORE_NAME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///naturescrates.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
