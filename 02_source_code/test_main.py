from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_rooms():
    # Send GET request to the rooms endpoint
    response = client.get("/api/rooms")
    
    # Check that status code is 200 OK
    assert response.status_code == 200
    
    # Check that response data is a list
    data = response.json()
    assert isinstance(data, list)
    
    # If database contains rooms, verify the data structure of the first item
    if len(data) > 0:
        assert "name" in data[0]
        assert "description" in data[0]