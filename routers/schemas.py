from pydantic import BaseModel
from typing import Optional

class TokenData(BaseModel):
    id:Optional[str] =None
      
class LoginRequest(BaseModel):
    username : str
    password : str
    
    
class Token(BaseModel):
    access_token :str
    token_type :str