#helper func/common func

from passlib.context import CryptContext

pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')

fake_user_db={
    'johndoe':{
        'username':'johndoe',
        'hashed_password':pwd_context.hash('secret123')
    }
}


def get_user(username:str):
    user=fake_user_db.get(username)
    return user

def verify_password(plain_pass,hashed_pass):
    return pwd_context.verify(plain_pass,hashed_pass)