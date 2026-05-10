from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_name:str
    database_user:str 
    database_password:str
    database_host:str
    database_port:int
    SECRET_KEY:str 
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int 

    class Config:
        env_file = '.env'


settings=Settings()