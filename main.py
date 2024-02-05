from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:str
    content:str

memos = []


app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모 추가에 성공했습니다'

@app.get("/memos")
def read_memo():
    return memos
    
@app.delete("/memos/{memo_id}")    
def delete_memo(memo_id):
    for index,memo in enumerate(memos):
        if memo.id==memo_id:
            memos.pop(index)
            return '성공했습니다.'
    return '그런 메모는 없습니다.'    

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):

@app.delete("/memos/{memo_id}")


@app.mount("/",StaticFiles(directory='static',html=True), name='static')