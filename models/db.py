from os import environ
from dotenv import load_dotenv
import pymysql.cursors
USE_DOTENV = environ.get("USE_DOTENV")

if(USE_DOTENV):
    load_dotenv()

def db():
    return pymysql.connect(host=environ.get("DB_HOST"),
                             user=environ.get("DB_USER"),
                             password=environ.get("DB_PASSWORD"),
                             database=environ.get("DB_HOST"),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

