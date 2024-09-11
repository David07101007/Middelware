from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_pokemon_general():
    response = client.get("/api/general/pikachu")
    assert response.status_code == 200
    assert response.json()["name"] == "pikachu"

def test_get_pokemon_not_found():
    response = client.get("/api/general/notarealpokemon")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon not found"
