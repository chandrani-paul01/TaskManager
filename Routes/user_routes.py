from fastapi import APIRouter,status,Depends
from Dao import  users_dao
from Misc import validations
from Main import db_connect

router = APIRouter(tags=['Users'])

@router.post('/users',status_code=status.HTTP_201_CREATED)
def insertUsers(data:validations.User_IncomingValidation,connection=Depends(db_connect.getDB)):
    return users_dao.insertUsers(connection,dict(data))