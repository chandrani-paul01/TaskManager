import jwt
from jwt import PyJWTError
from datetime import datetime,timedelta
from Misc import validations
from fastapi import Depends,status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from Main.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_token(payload:dict):
    to_encode = payload.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentialException):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        # print(payload)
        user_id:str =payload.get('userid')

        if user_id is None :
            raise credentialException
        
        tokenData = validations.TokenData(userid=user_id)
    except PyJWTError:
        raise credentialException
    
    return tokenData

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail='Could Not Validate Credentials', 
                                          headers={'WWW-Authenticate':'Bearer'})
    return verify_access_token(token,credentials_exception)

