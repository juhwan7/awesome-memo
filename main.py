from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
app = FastAPI()


class Memo(BaseModel):
    id: str
    content: str


# class Me:
#     def 이름():
#         print('김주환')
#     def 나이():
#         print('22살')
#     def MBTI():
#         print('INFJ');

memos = []


@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return '성공했습니다. '


@app.get("/memos")
def read_memo():

    return memos


@app.put("/memos/{memo_id}")
def put_memo(req_memo: Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return "이 id를가진 메모는 없습니다."


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return '삭제되었습니다.'
    return "이 id를가진 메모는 없습니다."


app.mount("/", StaticFiles(directory='static', html=True), name='static')

# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# app = FastAPI()


# class Memo(BaseModel):
#     id: str
#     content: str


# # class Me:
# #     def 이름():
# #         print('김주환')
# #     def 나이():
# #         print('22살')
# #     def MBTI():
# #         print('INFJ');

# memos = []


# @app.post("/memos")
# def create_memo(memo: Memo):
#     memos.append(memo)
#     return '성공했습니다. '


# @app.get("/memos")
# def read_memo():

#     return memos


# @app.put("/memos/{memo_id}")
# def put_memo(req_memo: Memo):
#     for memo in memos:
#         if memo.id == req_memo.id:
#             memo.content = req_memo.content
#             return '성공했습니다.'
#     return "이 id를가진 메모는 없습니다."


# @app.delete("/memos/{memo_id}")
# def delete_memo(memo_id):
#     for index, memo in enumerate(memos):
#         if memo.id == memo_id:
#             memos.pop(index)
#             return '삭제되었습니다.'
#     return "이 id를가진 메모는 없습니다."


# app.mount("/", StaticFiles(directory='static', html=True), name='static')

