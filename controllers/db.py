import mysql.connector
import os

# Get MySQL container connection details from environment variables
def connect():
    db_host = os.environ.get('DB_HOST', '103.101.224.67')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', 'Password')
    db_name = os.environ.get('DB_NAME', 'sim_rs')
    db_port = os.environ.get('DB_PORT','13306')
    
    # Establish a connection to the MySQL container
    return  mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port
    )