import os
from mongoengine import connect

def connection():
    try:
        connection_params = {
            'host': 'your_mongo_connection_string',  # Replace with your MongoDB connection string
            'connect': True,
            'alias': 'default'
        }

        use_db_auth = bool(int(os.environ.get('USE_DB_AUTH', 0)))
        if use_db_auth:
            connection_params['username'] = os.environ.get('MONGO_USERNAME')
            connection_params['password'] = os.environ.get('MONGO_PASSWORD')

        connect(**connection_params)
        print("Connected to database.")
    except Exception as error:
        print("Could not connect to database.", error)

