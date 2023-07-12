from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    type: str
    full_name: str
    username: str
    email: str
    password: str
    submitted_by: str
    
    class Config:
        orm_mode =True
        
            
class DepartmentCreate(BaseModel):
    department_name: str
    submitted_by: str
    
    class Config:
        orm_mode =True
        
        
class StudentCreate(BaseModel):
    full_name: str
    department_id: str
    classs: str
    submitted_by: str
    
    class Config:
        orm_mode =True
