from decouple import config


DATABASE_URL = config("DATABASE_URL")
DATABASE_NAME = config("DATABASE_NAME")
