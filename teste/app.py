from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) #Name para executar de forma manual

#Crud Create Read Update Delete

tasks = []
tasks_id_control = 1 #Padronizador

@app.route("/tasks", methods = ['POST'])
def create_task():

    global tasks_id_control

    data = request.get_json()

    new_task = Task(id = tasks_id_control, title = data.get("title"), description = data.get("description", ""))

    tasks_id_control += 1

    tasks.append(new_task)

    print(tasks)

    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods = ['GET'])
def get_tasks():

    task_list = [task.to_dict() for task in tasks]

    output = {"tasks": [task_list], "total_tasks": len(task_list)}
    return jsonify(output)

@app.route("/tasks/<int:id_task>", methods = ['GET'])
def get_task(id_task):
    for task in tasks:
        if task.id == id_task:
            return jsonify(task.to_dict())
        
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

@app.route("/user/<int:username_id>")
def show_user(username_id):
    print(username_id)
    print(type(username_id))
    return str(username_id)

if __name__ == "__main__":
    app.run(debug = True) #Uso apenas em desenvolvimento local

#variavel = 0
#def metodo_():
#  global variavel
#   variavel += 1
# return None