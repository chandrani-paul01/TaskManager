from pydantic import BaseModel
from typing import Optional

class Task_IncomingValidation(BaseModel):
    TaskName:str
    Description:Optional[str]=''
    IsComplete:bool=False

class Task_IncomingPatchValidation(BaseModel):
    TaskName: Optional[str] = None
    Description: Optional[str] = None
    IsComplete: Optional[bool] = None

class Task_OutgoingValidation(BaseModel):
    TaskName:str
    Description:str
    IsComplete:bool
    CreatedDate:str
    # userID:int

class User_IncomingValidation(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    userid:Optional[str]