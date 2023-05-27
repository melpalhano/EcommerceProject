from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "produto"

@app.post("/produto")
def create_produto():
    return "create produto"

@app.get("/produto/{id}")
def read_produto(id: int):
    return "read produto with id {id}"

@app.get("/produto")
def read_produto_list():
    return "read all produto"

@app.put("/produto/{id}")
def update_produto(id: int):
    return "update produto item with id {id}"

@app.delete("/produto/{id}")
def delete_produto(id: int):
    return "delete produto item with id {id}"
