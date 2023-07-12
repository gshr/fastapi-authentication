
from fastapi import APIRouter,Depends
from db import Session,get_session,Department
from models import DepartmentCreate
from .login import current_user
import uuid
router = APIRouter(
    tags = ['Departments']
)


@router.post("/departments/",status_code=201)
def create_department(department:DepartmentCreate,
                      session: Session = Depends(get_session)
                      ):
    data = Department(id=str(uuid.uuid4()),**department.dict())
    session.add(data)
    session.commit()
    session.refresh(data)
    return data
    
@router.get("/departments/")
def create_department(session: Session = Depends(get_session),
                       current_user=Depends(current_user)):
    departments=session.query(Department).all()
    return departments
    
