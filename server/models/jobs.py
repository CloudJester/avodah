from typing import Union

class JobInternal():
    id: str
    name: str
    image: Union[str, None] = None

    def __init__(self, 
        id: str,
        name: str, 
        image: Union[str, None]):
        self.id = id
        self.name = name
        self.image = image