from typing import List
from pydantic import BaseModel
from .pagination_response import PaginationResponse


class UserItemResponse(BaseModel):
    id: int
    uuid: str
    email: str
    first_name: str = ''
    last_name: str = ''
    job_title: str = None
    phone: str = None


class UserPaginationResponse(PaginationResponse):
    data: List[UserItemResponse] = []
