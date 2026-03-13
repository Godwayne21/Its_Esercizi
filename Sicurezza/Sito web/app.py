from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    search_query = request.args.get('query', '')
    
    # Creiamo la risposta
    resp = make_response(render_template('index.html', q=search_query))
    
    # DISABILITIAMO la protezione XSS del browser per permettere l'esercitazione
    resp.headers['X-XSS-Protection'] = '0'
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5000)