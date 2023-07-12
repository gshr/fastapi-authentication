


from fastapi import APIRouter,Depends,HTTPException
from db import Session,get_session,Student,Department
from .login import current_user
from models import StudentCreate
import uuid

router = APIRouter(
    tags = ['Students']
)



@router.get("/students/")
def get_students(session: Session = Depends(get_session)):
    students=session.query(Student).all()
    return students

@router.get("/students/{id}")
def get_students(id:str,
                 session: Session = Depends(get_session),
                current_user=Depends(current_user)):
    print(current_user.id)
    print(id)
    students=session.query(Student).filter(Student.id==id).first()
    if students:
        return students
    raise HTTPException(status_code=404, detail=f"Student with {id} not found")
    
       
@router.post("/student/",status_code=201)
def create_student(user:StudentCreate,
                   session: Session = Depends(get_session)
                 ):
    department = session.query(Department).filter(Department.id==user.department_id).first()
    if department:
        try:
            students = Student(id=str(uuid.uuid4()),**user.dict())
            session.add(students)
            session.commit()
            session.refresh(students)
            return students
        except Exception as e:
            return e
    raise HTTPException(status_code=404, detail="Department not found")