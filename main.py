from fastapi import FastAPI,Depends
from db import Base,engine
from routers import users,department,students,login

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(department.router)
app.include_router(students.router)
app.include_router(login.router)



    
    
    
