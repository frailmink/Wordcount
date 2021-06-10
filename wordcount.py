from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Body(BaseModel):
    string: str

app = FastAPI()

@app.post("/word_count/")
async def word_count(body: Body):
    string = body.string
    count = 0
    list = string.split(" ")
    for i in range(len(list)):
        if list[i] != "":
           count = count + 1
    return {"word_count": count}

@app.get("/")
async def root():
    return HTMLResponse(open("index.html", "rt").read())
