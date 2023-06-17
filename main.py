from fastapi import FastAPI
from database import Base, engine, Produto
from pydantic import BaseModel
from sqlalchemy.orm import Session

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

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
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    dados = {'pagina': 'Home'}
    return templates.TemplateResponse("index.html", {"request": request, 'dados':dados})

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

    if produto is not None:
        produto.nome = novos_dados_produto.nome
        produto.quantidade = novos_dados_produto.quantidade
        produto.valor = novos_dados_produto.valor
        session.commit()
        session.close()
        return produto
    else:
        session.close()
        return 'Produto não encontrado!'

@app.delete("/produto/{id}")
def delete_produto(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    produto = session.query(Produto).filter(Produto.id == id).first()
    if(produto.quantidade > 0):
        return -1
    
    session.delete(produto)
    session.commit()
    session.close()
    #return "delete produto item with id {id}"
