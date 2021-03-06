import os

from cryptography.fernet import Fernet

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
OTP_LENGTH = int(os.getenv("OTP_LENGTH", "8"))
OTP_LIFETIME = int(os.getenv("OTP_LIFETIME", "5"))
MAGIC_LIFETIME = int(os.getenv("MAGIC_LIFETIME", "5"))
HOST = os.getenv("HOST")
MAILGUN_KEY = os.getenv("MAILGUN_KEY")
MAILGUN_ENDPOINT = os.getenv("MAILGUN_ENDPOINT")
FROM_ADDRESS = os.getenv("FROM_ADDRESS")
VERSION = os.getenv("APP_VERSION")
DB_USERNAME = os.getenv("DB_USERNAME", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "27017")
DB_NAME = os.getenv("DB_NAME", "app")
ISSUER = os.getenv("ISSUER", "http://localhost:8080")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
FERNET_KEY = os.getenv("FERNET_KEY")
FERNET = Fernet(FERNET_KEY)
