import os

APP_ENV = os.getenv('APP_ENV', 'developement')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '0000')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'tarification')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'tarification_test')
