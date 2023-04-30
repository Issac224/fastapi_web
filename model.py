#from pydantic import BaseModel

# class PacktBook(BaseModel):
#     i: int
#     Name: str
#     Publishers :str
#     Isbn :str

# class Item(BaseModel):
#     item: str
#     status : StopAsyncIteration
    
    
# #중첩 모델 만들기
# class Todo(BaseModel):
#     id: int
#     item: Item

# #중첩 모델로 형식 새롭게 만들어서
# #딕셔너리 안에 딕셔너리를 넣어야 한다.

from pydantic import BaseModel

# class PacktBook(BaseModel):
#     id: int
#     Name: str
#     Publishers: str
#     Isbn: str


class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: str