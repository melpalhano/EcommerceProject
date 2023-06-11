from fastapi import FastAPI
from database import Base, engine, Produto
from pydantic import BaseModel
from sqlalchemy.orm import Session

class ProdutoRequest(BaseModel):
    nome: str
    quantidade: int
    valor: int


Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return "produto"

@app.post("/produto")
def create_produto(produto: ProdutoRequest):
    session = Session(bind=engine, expire_on_commit=False)
    produto = Produto(nome=produto.nome, quantidade=produto.quantidade, valor=produto.valor)
    session.add(produto)
    session.commit()
    id = produto.id
    session.close()
    return {"id": id, "nome": produto.nome}

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
    session = Session(bind=engine, expire_on_commit=False)
    produto = session.query(Produto).filter(Produto.id == id).first()
    session.delete(produto)
    session.commit()
    session.close()
    # return f"delete produto item with id {id}"
