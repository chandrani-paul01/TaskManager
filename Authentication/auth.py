from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Misc import validations,utilities
from Dao import users_dao
from Main import db_connect
from Authentication import oauth2

router=APIRouter(tags=["Authetication"])

@router.post("/login",response_model=validations.Token)
def login(cred:OAuth2PasswordRequestForm = Depends()):

    userfound=users_dao.getUserByUserName(db_connect.getDB(),cred.username)

    if not userfound:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Incorrect Credentials')
    
    hashed_password=utilities.hashPassword(cred.password)

    if not utilities.verifyPassword(cred.password,hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Incorrect Credentials')
    
    return {"acess_token":oauth2.create_token({"userid":userfound[1]}),
                "token_type":"bearer"}




