import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
task_id_list = []
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descricao"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json

    task_id_list.append(response_json['id'])# Muito importante para o entendimento: estamos armazenando apenas o id e não todos atributos
    tasks.append(response_json)


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if task_id_list:
        task_id = task_id_list[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']


def test_update_task():
    if task_id_list:
        task_id = task_id_list[0]

        payload = {
            "title": "title_a", 
            "description": "descr_a", 
            "completed": True
            }
        
        #Atualizando tarefa com o json do payload com PUT (PUT atualiza todos os atributos)
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200

        response_json = response.json()

        assert "message" in response_json

        #Verificando se foi atualizado
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

def test_delete_task():
    if task_id_list:
        task_id = task_id_list[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404