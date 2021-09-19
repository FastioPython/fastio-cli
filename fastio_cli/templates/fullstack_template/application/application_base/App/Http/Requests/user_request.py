from pydantic import BaseModel
from typing import Optional


class UserCreateRequest(BaseModel):
    email: str= None
    firstName: str= None
    id: int= None
    lastName: str= None
    password: str= None
    phone: str= None
    userStatus: int= None
    username: str= None


class UserUpdateRequest(BaseModel):
    email: Optional[str]= None
    firstName: Optional[str]= None
    id: Optional[int]= None
    lastName: Optional[str]= None
    password: Optional[str]= None
    phone: Optional[str]= None
    userStatus: Optional[int]= None
    username: Optional[str]= None