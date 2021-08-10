from typing import Optional

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float



app = FastAPI()


@app.get("/")
def read_root(user: Optional[str] = Header("123")):
    return {"user-agent": user}

@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="meucookie", value="cookie123")
    return {"cookie": True}

@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"Cookie": meucookie}

@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p": p}

@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]