from flask import Flask, request, render_template

app = Flask(__name__)

# Un "database" simulato in memoria
USERS_DB = {
    "1": {"name": "Alice (Utente Standard)", "role": "user", "secret": "Il mio PIN del bancomat è 1234."},
    "2": {"name": "Bob (Utente Standard)", "role": "user", "secret": "Ho nascosto le chiavi di casa sotto lo zerbino."},
    "3": {"name": "Amministratore di Sistema", "role": "admin", "secret": "FLAG{BAC_Bypassed_Admin_Dashboard_8829}"}
}

@app.route('/')
def home():
    # 🚨 VULNERABILITÀ: L'applicazione prende l'ID direttamente dall'URL
    # e lo usa per mostrare i dati, senza controllare se chi sta
    # visualizzando la pagina sia effettivamente quell'utente.
    
    # Di default carichiamo il profilo di Alice (ID=1)
    user_id = request.args.get('user_id', '1')
    
    # Recuperiamo i dati dal "database"
    user_data = USERS_DB.get(user_id)
    
    return render_template('index.html', user_data=user_data, current_id=user_id)

if __name__ == '__main__':
    # Flask ora gira sulla 5000. 
    # L'Agente riceve sulla 32456, applica il .ars e poi passa tutto alla 5000.
    app.run(debug=True, port=5000)