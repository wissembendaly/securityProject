import mysql.connector
from mysql.connector import Error

class DbConnector:
    
    user= 'root'
    password= None
    host= 'localhost',
    database= 'securityproject'

    # username:str ='root'
    # password:str = None
    # hostName:str ='127.0.0.1'
    # # dbName:str ='securityproject'
    
    connection= None
    cursor = None
    def __init__(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='securityproject',
                                         user='root',
                                         password=None)

            self.connection=connection
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor(buffered=True)
                self.cursor=cursor
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                
        except Error as e:
            print("Error while connecting to MySQL", e)
        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")