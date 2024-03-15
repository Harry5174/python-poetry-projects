# test_main.py

from fastapi.testclient import TestClient
from src.todo.routes.main import app

client = TestClient(app)

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_todo_by_id():
    response = client.get("/todos/4")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "id" in response.json()
    assert "title" in response.json()
    assert "description" in response.json()

def test_create_todo():
    todo_data = {"title": "Test Todo", "description": "Test Description"}
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == 200
    assert response.json()["title"] == todo_data["title"]
    assert response.json()["description"] == todo_data["description"]

def test_update_todo():
    todo_id = 17
    updated_data = {"title": "Updated Todo", "description": "Updated Description"}
    response = client.put(f"/todos/{todo_id}", json=updated_data)
    assert response.status_code == 200


def test_delete_todo():
    response = client.delete("/todos/10")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"
