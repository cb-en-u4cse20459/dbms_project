import mysql.connector
from mysql.connector import Error
def create_connection(host_name,port_name,user_name,user_password,db_name):
    connection=None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port=port_name,
            user=user_name,
            database=db_name,
            passwd=user_password
        )
        print("Connection to mysql successful")
    except Error as e:
        print("The error '{}' occurred".format(e))
    return connection
connection =create_connection("localhost","3306","admin","password","boat")
def exec_query(connection,database_query,mode):
    cursor=connection.cursor()
    result =None
    try:
        print(cursor.execute(database_query))
        if (mode=="selection"):        
            result =cursor.fetchall()
            return result
        elif (mode=="insertion"):
            connection.commit()
            print("Task completed successfully")
    except Error as e:
        print("The error '{}' occurred".format(e))
create_users = "create table type(color varchar,sizer int);"
print(exec_query(connection, create_users,"insertion"))
