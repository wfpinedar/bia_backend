from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/api/v1/meter/usage?date=2022-10-26&period=monthly&skip=0&limit=100")
    assert response.status_code == 200
    
def test_data_length():
    response = client.get("/api/v1/meter/usage?date=2022-10-26&period=monthly&skip=0&limit=100")
    assert len(response.json()) == 19
    
def test_data_first():
    response = client.get("/api/v1/meter/usage?date=2022-10-26&period=monthly&skip=0&limit=100")
    assert response.json()[0] == {'meter_date': '2022-10-12T00:00:00' , 'value': 539.76}