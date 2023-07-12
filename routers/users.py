
from fastapi import APIRouter,Depends
from db import Session,get_session,User
from models import UserCreateRequest

router = APIRouter(
    tags = ['Users']
)



@router.get("/users/")
def get_users(session: Session = Depends(get_session)):
    data=session.query(User).all()
    return data
       
@router.post("/users/",status_code=201)
def create_users(user:UserCreateRequest,session: Session = Depends(get_session)):
    try:
        users = User(**user.dict())
        session.add(users)
        session.commit()
        session.refresh(users)
        return users
    except Exception as e:
        print(e)
        return e