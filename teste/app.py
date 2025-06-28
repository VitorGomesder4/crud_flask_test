from flask import Flask

app = Flask(__name__) #Name para executar de forma manual

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/about")
def about():
    return "Pagina Sobre kk"

if __name__ == "__main__":
    app.run(debug=True) #Uso apenas em desenvolvimento local