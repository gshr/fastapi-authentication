import uuid
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session() :
    with Session(engine) as session:
        yield session

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    type = Column(String)
    full_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Department(Base):
    __tablename__ = "departments"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    department_name = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)

class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    full_name = Column(String)
    department_id = Column(String, ForeignKey("departments.id"))
    classs = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)

class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    course_name = Column(String)
    department_id = Column(String, ForeignKey("departments.id"))
    semester = Column(String)
    classs = Column(String)
    lecture_hours = Column(Integer)
    submitted_by = Column(String)
    updated_at =Column(DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)

class AttendanceLog(Base):
    __tablename__ = "attendance_logs"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    present = Column(Boolean)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)


