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
        {"nome": "Produto 5", "quantidade": 50, "valor": 500},
    ]

def test_create_produto(sample_produto):
    client = TestClient(app)
    response = client.post("/produto", json=sample_produto[0])
    assert response.status_code == 200
    assert response.json()["nome"] == sample_produto[0]["nome"]





