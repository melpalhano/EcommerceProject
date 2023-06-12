import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def sample_produto():
    return [
        {"nome": "Produto 1", "quantidade": 10, "valor": 100},
        {"nome": "Produto 2", "quantidade": 20, "valor": 200},
        {"nome": "Produto 3", "quantidade": 30, "valor": 300},
        {"nome": "Produto 4", "quantidade": 40, "valor": 400},
        {"nome": "Produto 5", "quantidade": 50, "valor": 500}
    ]

@pytest.fixture
def sample_id():
    return [
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
        {"id": 5},
    ]

def test_create_produto(sample_produto):
    client = TestClient(app)
    response = client.post("/produto", json=sample_produto[0])
    assert response.status_code == 200
    assert response.json()["nome"] == sample_produto[0]["nome"]

def test_detele_produto(sample_produto):
    client = TestClient(app)
    response = client.post("/produto", json=sample_produto[0])
    response2 = client.delete(f"/produto/{response.json()['id']}")
    assert response2.status_code == 200

def test_read_produto(sample_produto):
    client = TestClient(app)
    response = client.post("/produto", json=sample_produto[0])
    response2 = client.get(f"produto/{response.json()['id']}")
    assert response2.json()['nome'] == sample_produto[0]['nome']




def test_read_produto_all(sample_produto):
    client = TestClient(app)
    produtos_buscados = client.get('/produto')
    qt_antes = len(produtos_buscados.json())
    for indice in range(0,5):
        client.post('/produto', json=sample_produto[indice])
    produtos_buscados = client.get('/produto')
    qt_depois = len(produtos_buscados.json())
   
    assert (qt_depois - qt_antes == 5)



    

