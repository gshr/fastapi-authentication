
from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from db import Session,get_session,User
from .schemas import TokenData,Token
from datetime   import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags = ['Authentication']
)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth_schemes = OAuth2PasswordBearer(tokenUrl = 'login')

def create_access_token(data:dict):
    
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str,cred_exception):
    try:
        payload=jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        token_id:str=payload.get('user_id')
        if id is None:
            return cred_exception
        
        token_data = TokenData(id=token_id)
        
    except JWTError:
        raise cred_exception
    
    return token_data
    
def current_user(token:str = Depends(oauth_schemes),db:Session =Depends(get_session)):
    cred_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                  detail=f"token not validate Credentails",
                                  headers={"WWW-Authenticate":'Bearer '})
    token=verify_access_token(token, cred_exception)
    user=db.query(User).filter(User.id == token.id).first()    
    return user


@router.post('/login',response_model=Token)
def login(user_credential : OAuth2PasswordRequestForm = Depends(),session:Session =Depends(get_session)):
    print(user_credential.username,user_credential.password)
    user=session.query(User).filter(
        User.username==user_credential.username).first()
    print(user.password,user.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    if user_credential.password != user.password:
        print('-----------')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    access_token = create_access_token(data={'user_id': user.id})
    print(access_token)
    
    return {"access_token":access_token,"token_type":"bearer" }
    


