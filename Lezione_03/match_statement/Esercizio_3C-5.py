# Esercizio 3C-5
'''
Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. 
Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"
'''

utente = {"nome": "", "ruolo": "", "eta": ""}


utente["nome"] = str(input("Inserisci il tuo nome: "))
utente["ruolo"]= str(input("Insreisci il tuo ruolo: "))
utente["eta"] = int(input("Inserisci la tua età: "))

match utente:

    case utente if utente["ruolo"] == "admin" :
        print(f"{utente['nome']} ha accesso completo a tutte le funzionalità.")

    case utente if utente["ruolo"] == "moderatore" :
        print(f"{utente['nome']} può gestire i contenuti ma non modificare le impostazioni.")

    case utente if utente["ruolo"] == "utente adulto" or utente["eta"] >= 18 :
        print(f"{utente['nome']} ha accesso standard a tutti i servizi.")

    case utente if utente["ruolo"] == "utente minorenne" or utente["eta"] <= 18 :
        print(f"{utente['nome']} ha accesso limitato! Alcune funzionalità sono bloccate.")

    case utente if utente["ruolo"] == "ospite":
        print("attenzione! Ruolo non riconsciuto! Accesso Negato!")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
