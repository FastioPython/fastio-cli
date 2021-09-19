from typing import List
from pydantic import BaseModel


class PaginationResponse(BaseModel):
    total: int
    per_page: int
    last_page: int
    current_page: int
    data: List = []
