from fastapi import FastAPI
from fastapi import Form
from pydantic import BaseModel
import pymongo
from typing import List

db_client = pymongo.MongoClient("mongodb://pythonproject17-db-1")
db = db_client["root"]
post = db["post"]



app = FastAPI()
class Post(BaseModel):
    sting_value: str = "value"
    int_value: int = 0
    bool_value: str = False

class id(BaseModel):
    id: str = "value"

class Get(BaseModel):
    sting_value: str = "value"
    int_value: int = 0
    bool_value: str = False
    list: List[id]

@app.post("/")
def root(massage: Post):
    post.insert_one({"something":"something"})
    return {"json":Post(string_value=massage.sting_value, int_value=massage.int_value, bool_value=massage.bool_value)}

@app.post("/form")
def root(sting_value_: str = Form(...),int_value_: int = Form(...),bool_value_: bool = Form(...)):
    post.insert_one({"something": "something"})
    return {"json":Post(string_value=sting_value_, int_value=int_value_, bool_value=bool_value_)}

@app.get("/")
def root():
    all = post.find()
    list_out = []
    for elements in all:
        list_out.append(id(id=str(elements["_id"])))
    return {"json":Get(list=list_out)}