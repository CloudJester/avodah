from pydantic import BaseModel
from typing import Union

class Job(BaseModel):
    id: Union[str, None] = None
    name: str
    image: Union[str, None] = None