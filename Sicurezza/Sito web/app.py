from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Funzione per creare un DB SQLite in memoria "al volo"
def get_db_connection():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Creiamo la tabella e inseriamo i nostri utenti
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, role TEXT, secret TEXT)''')
    users_data = [
        (1, 'Alice', 'user', 'Il mio PIN del bancomat è 1234.'),
        (2, 'Bob', 'user', 'Ho nascosto le chiavi di casa sotto lo zerbino.'),
        (3, 'Admin', 'admin', 'FLAG{SQLi_WAF_Testing_9921}')
    ]
    c.executemany('INSERT INTO users VALUES (?,?,?,?)', users_data)
    conn.commit()
    return conn

@app.route('/')
def home():
    # L'utente cerca un nome tramite la barra di ricerca
    search_query = request.args.get('search', 'Alice')
    
    conn = get_db_connection()
    c = conn.cursor()
    
    # 🚨 VULNERABILITÀ SQL INJECTION: Il payload dell'utente viene 
    # concatenato direttamente nella stringa SQL senza sanitizzazione.
    sql_statement = f"SELECT * FROM users WHERE name = '{search_query}'"
    
    results = []
    error_msg = None
    
    try:
        c.execute(sql_statement)
        results = c.fetchall()
    except sqlite3.Error as e:
        # Mostriamo l'errore SQL a schermo (pessima pratica, ottima per i lab!)
        error_msg = str(e)
        
    return render_template('index.html', 
                           search_query=search_query, 
                           sql_statement=sql_statement, 
                           results=results, 
                           error_msg=error_msg)

if __name__ == '__main__':
    # Flask gira sulla 5000. Il WAF (l'agente) starà sulla 32456.
    app.run(debug=True, port=5000)