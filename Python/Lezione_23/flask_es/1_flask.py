from flask import Flask

app = Flask (__name__)

@app.route('/')
def home()-> str:
    return "<h1>Hello World 🛞🛞💉👴🏻</h1>"

@app.route('/about')
def about()-> str:
    return "<h1>Sono Filippino</h1>"

@app.route('/user/<nome>')
def user(nome:str)-> str:
    return f"User: {nome}"

@app.route('/square/<int:n>')
def square(n:int)->str:
    return "Square:" + str(n**2)

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int, b:int)-> str:
    return "Sum:" + str(a+b)