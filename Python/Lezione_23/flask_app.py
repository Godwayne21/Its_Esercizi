from flask import Flask, url_for

app = Flask (__name__)
#1. metodo app.run (debug=True, host='127.0.0.1', port=5000) comando(python3.11 flask_app.py)
#In production, set debug False 

# 2. metodo comando (flask --app "nome file senza estesione(.py)" run )
@app.route('/')
def home()-> str:
    return "<h1>Hello World 🛞🛞💉👴🏻</h1>"

#3. metodo flask run  (solo se il il file si chiama "app.py")

#metodo 2 e 3 migliori

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age:int) -> str:
 return f"Profilo di {username}, età {age}"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
 return f"Post {post_id}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe', age = 43))
    print(url_for('show_post', post_id=42))