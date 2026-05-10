from fastapi import APIRouter,status,Depends
from Dao import  tasks_dao
from Misc import validations
from Main import db_connect
from Authentication import oauth2

router = APIRouter(tags=['Tasks'])

@router.get('/')
def testget():
    return {'message':'hello'}

@router.get('/tasks')
def getTasks(connection=Depends(db_connect.getDB),user_token: int =Depends(oauth2.get_current_user)):
    #list of tuples to dict if Response_Model is added
    return tasks_dao.getTasks(connection,user_token.userid)

# Add the outgoing response model
@router.post('/tasks',status_code=status.HTTP_201_CREATED)
def insertTasks(data:validations.Task_IncomingValidation,
                connection=Depends(db_connect.getDB),
                  user_token: int =Depends(oauth2.get_current_user) ):
    # print(user_id)
    #user_token: int =Depends(oauth2.get_current_user) why type hint is not enforeced??
    return tasks_dao.insertTask(connection,dict(data),user_token.userid)

# Add the outgoing response model
@router.patch('/tasks/{TaskID}')
def updateTasks(TaskID:int,data:validations.Task_IncomingPatchValidation,connection=Depends(db_connect.getDB),
                user_token: int =Depends(oauth2.get_current_user)):
    return tasks_dao.updateTask(connection,TaskID,dict(data))

# Add the outgoing response model
@router.delete('/tasks/{TaskID}')
def deleteTasks(TaskID:int,connection=Depends(db_connect.getDB),user_token: int =Depends(oauth2.get_current_user)):
    return tasks_dao.deleteTask(connection,TaskID)
