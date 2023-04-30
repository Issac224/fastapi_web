# from fastapi import FastAPI
# from todos import todo_router

# app = FastAPI()

# @app.get("/")
# async def welcome() -> dict:
#     return{
#         "message" : "Hello world"
#     }

# @app.get("/name")
# async def welcome2() -> dict: #함수 이름은 딱히 상관 없다.
#     return{
#         "message" : "Hello world2"
#     }

# #async는 비동기 처리를 의미한다.
# #이거 다른 거 기다리지 않고 바로 실행

# # ->dict : 이건 return의 형식을 정해준다. 
# # return의 형식을 directory로 지정해준 것이다.


# #객체에 넣어준 후, 여기서 불러와서 사용
# app.include_router(todo_router)

from fastapi import FastAPI
from todos import todo_router

app = FastAPI()

# @app.get("/")
# async def welcome() -> dict:
#     return {
#         "message": "Hello World"
#     }

# @app.get("/name")
# async def welcome2() -> dict:
#     return {
#         "message": "Hello World2"
#     }


app.include_router(todo_router)