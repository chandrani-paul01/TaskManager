import psycopg2
from Main.config import settings

# print(settings.database_user)

def getDB():
    connection = psycopg2.connect(database=settings.database_name,
                                user=settings.database_user, 
                                password=settings.database_password, 
                                    host=settings.database_host,
                                    port=settings.database_port)
    return connection

# def getUserByUserName(conn,username):
#     cursor = conn.cursor()
#     cursor.execute("""SELECT * FROM public."Users" WHERE username = %s;""",(username,))
#     record = cursor.fetchone()
#     return record

# print(getUserByUserName(getDB(),'rani'))