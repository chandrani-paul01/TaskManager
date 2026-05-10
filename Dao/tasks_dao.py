#Optimize and Understand when and where to close the cursor and connection
# Try and Except for error handling

#Get Tasks
def getTasks(conn,user):

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM public."Tasks" where "UserID" = %s ;""",(user,))
    record = cursor.fetchall()
    return record

#Insert Tasks
def insertTask(conn,TaskDetails,user):

    try:
        cursor = conn.cursor()
        InsertQuery = """INSERT INTO public."Tasks"("TaskName", "Description","UserID")
                        VALUES (%s,%s,%s);"""
        values = (TaskDetails['TaskName'],TaskDetails['Description'],user)
        cursor.execute(InsertQuery,values)
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        return False

    

#Update Tasks   
def updateTask(conn, TaskID, TaskDetails):
    
    allowed_fields = ["TaskName", "Description", "IsComplete"]

    set_clauses = []
    values = []

    for key, value in TaskDetails.items():
        if key in allowed_fields and value != None:
            set_clauses.append(f'"{key}" = %s')
            values.append(value)

    # If nothing to update
    if not set_clauses:
        return "No valid fields to update"

    # Add task_id at the end
    values.append(TaskID)

    query = f'''
        UPDATE public."Tasks"
        SET {', '.join(set_clauses)}
        WHERE "TaskID" = %s
    '''

    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()

    return cur.rowcount

#Delete Tasks
def deleteTask(conn,TaskID):
    cursor = conn.cursor()
    DeleteQuery = """DELETE FROM public."Tasks" WHERE "TaskID" = %s"""
    values = (TaskID,)
    cursor.execute(DeleteQuery,values)
    conn.commit()
    return cursor.rowcount

# import psycopg2
# connection = psycopg2.connect(database="TaskManager",
#                                user="postgres", 
#                                password="1234", 
#                                 host='localhost',
#                                  port=5432)
# insertTask(connection,{'TaskName':'UpdateData','Description':'InDB'},1)
# # updateTask(connection,1,{'TaskName':'UpdateData','Description':'InDB'})
