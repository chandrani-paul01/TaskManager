from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def hashPassword(password):
    hashedString= pwd_context.hash(password)
    return hashedString

def verifyPassword(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

