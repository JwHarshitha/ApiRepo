from sqlalchemy import create_engine
import urllib.parse

class DBConnectors:
    def __init__(self) -> None:
        pass

    def create_mysql_engine(self):
        username = 'jwalaharshitha'
        password = 'Tredence@123'
        host = 'localhost'
        database_name = 'payroll_analytics_dev'
        encoded_password = urllib.parse.quote_plus(password)
        connection_string = f'mysql+mysqlconnector://{username}:{encoded_password}@{host}/{database_name}'
        engine = create_engine(connection_string)
        return engine
