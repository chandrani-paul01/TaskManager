from Misc import utilities

#Get Users
def getUserByUserName(conn,username):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM public."Users" WHERE username = %s;""",(username,))
    record = cursor.fetchone()
    return record

#Insert Users
def insertUsers(conn,UserDetails):

    cursor = conn.cursor()
    insertquery = """INSERT INTO public."Users"(username, password) VALUES (%s,%s);"""
    hashed_password=utilities.hashPassword(UserDetails['password'])
    values = (UserDetails['username'],hashed_password)
    cursor.execute(insertquery,values)
    conn.commit()

    return cursor.rowcount