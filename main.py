from fastapi import FastAPI
from database import Base, engine, Produto
from pydantic import BaseModel
from sqlalchemy.orm import Session

class ProdutoRequest(BaseModel):
    nome: str
    quantidade: int
    valor: int


class ProdutoUpdateRequest(BaseModel):
    id: int
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
    session = Session(bind=engine, expire_on_commit=False)
    produto = session.query(Produto).get(id)
    session.close()
    return produto

@app.get("/produto")
def read_produto_list():
    session = Session(bind=engine, expire_on_commit=False)
    produtos = session.query(Produto).all()
    session.close()
    return produtos

@app.put("/produto")
def update_produto(novos_dados_produto: ProdutoUpdateRequest):
    session = Session(bind=engine, expire_on_commit=False)
    produto = session.query(Produto).get(novos_dados_produto.id)
    produto.nome = novos_dados_produto.nome
    produto.quantidade = novos_dados_produto.quantidade
    produto.valor = novos_dados_produto.valor
    session.commit()
    session.close()
    return produto


@app.delete("/produto/{id}")
def delete_produto(id: int):
    return "delete produto item with id {id}"
