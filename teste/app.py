from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) #Name para executar de forma manual

#Crud Create Read Update Delete

tasks = []
tasks_id_control = 1 #Padronizador


@app.route("/tasks", methods = ['POST']) #Create
def create_task():

    global tasks_id_control

    data = request.get_json()

    new_task = Task(id = tasks_id_control, title = data.get("title"), description = data.get("description", ""))

    tasks_id_control += 1

    tasks.append(new_task)

    print(tasks)

    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}) #RESPONSE


@app.route("/tasks", methods = ['GET']) #Read
def get_tasks():

    task_list = [task.to_dict() for task in tasks]

    output = {"tasks": [task_list], "total_tasks": len(task_list)}
    return jsonify(output) #RESPONSE


@app.route("/tasks/<int:id_task>", methods = ['GET']) #Read por ID
def get_task(id_task):
    for task in tasks:
        if task.id == id_task:
            return jsonify(task.to_dict()) #RESPONSE
        
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404 #RESPONSE


@app.route("/tasks/<int:id>", methods = ['PUT']) #Update
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break #Apos achar e guardar a tarefa requerida break para não continuar o loop, perfomance

    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404 #RESPONSE
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    print(task)
    return jsonify({"message": "Atualização foi um Sucesso"}) #RESPONSE


@app.route("/tasks/<int:id>", methods = ['DELETE'])
def delete_task(id):
    task = None

    for t in tasks:
        if t.id == id:
            task = t
            break #Apos achar e guardar a tarefa requerida break para não continuar o loop, perfomance

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404 #RESPONSE
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"}) #RESPONSE





#@app.route("/user/<int:username_id>") #Exemplo de 'converter'
#def show_user(username_id):
#    print(username_id)
#    print(type(username_id))
#    return str(username_id)

if __name__ == "__main__":
    app.run(debug = True) #Uso apenas em desenvolvimento local

#variavel = 0
#def metodo_():
#  global variavel
#   variavel += 1
# return None