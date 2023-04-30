# from fastapi import APIRouter
# from model import Todo #id는 int형식 item은 str로 받도록 이거 검증하는 파일

# # router = APIRouter()

# # @router.get("/hello")
# # async def say_hello() ->dict:
# #     return{
# #         "message" : "Hello world"
# #     }

# # todo_router = APIRouter()
# # todo_list = [] # 원래 data base에서 정보를 넣고 빼고 해야함, 임시적으로 배열에서 넣고 빼는거 연습
# # @todo_router.post('/todo') #포스터 방식으로 시작
# # async def add_todo(todo: dict) -> dict:
# #     todo_list.append(todo)
# #     return{
# #         "message" : "Todo added successfuly."
# #     }
    
# # @todo_router.get('/todo') #포스터 방식으로 시작
# # async def retrieve_todos() -> dict:
# #     return{
# #         "message" : todo_list
# #     }
    

# # 함수를 바깥에 선언해주기 
# #Fast api의 메인 코드 실행하는 것과
# # 
# # 기능 있는 거 따로 두고, 가져오는 식으로 진행



# #검증할 때 썼던 코드
# # todo_router = APIRouter()
# # todo_list = [] # 원래 data base에서 정보를 넣고 빼고 해야함, 임시적으로 배열에서 넣고 빼는거 연습
# # @todo_router.post('/todo') #포스터 방식으로 시작
# # async def add_todo(todo: Todo) -> dict: #보내는 형식 주어졌다.
# #     todo_list.append(todo)
# #     return{
# #         "message" : "Todo added successfuly."
# #     }
    
# # @todo_router.get('/todo') #포스터 방식으로 시작
# # async def retrieve_todos() -> dict:
# #     return{
# #         "message" : todo_list
# #     }
    
#     # Todo 방식으로 하면 알아서 형식에 맞지 않는 것을 걸러낸다는 점에서 좋다 
    
    
# todo_router = APIRouter()
# todo_list = [] # 원래 data base에서 정보를 넣고 빼고 해야함, 임시적으로 배열에서 넣고 빼는거 연습
# @todo_router.post('/todo') #포스터 방식으로 시작
# async def add_todo(todo: Todo) -> dict: #보내는 형식 주어졌다.
#     todo_list.append(todo)
#     return{
#         "message" : "Todo added successfuly."
#     }
    
# @todo_router.get('/todo') #포스터 방식으로 시작
# async def retrieve_todos() -> dict:
#     return{
#         "todos" : todo_list
#     }

# @todo_router.get("/todo/{todo_id}")
# async def get_single_todo(todo_id :int) ->dict:
#     for todo in todo_list: #todo list에 접근, todo list의 원소가 todo에 저장
#         if todo.id == todo_id: 
#             return{
#                 "todo" : todo                
#             }
#     return{
#         "message" : "Todo with supplied ID dosen't exist."
#     }
    

from fastapi import APIRouter
from model import Todo

todo_router = APIRouter()

todo_list = []

# @router.get("/hello")
# async def say_hello() -> dict:
#     return {
#         "message": "Hello World"
#     }


@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message" : "Todo Added Successfully"
    }

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo (todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist"
    }