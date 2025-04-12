'''
Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
Ogni carta ha un valore compreso tra 2 e 11 inclusi.

Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere considerato 1 per evitare il "bust" (superare 21).
Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte e 
restituisce il valore totale della mano secondo le regole del Blackjack.

For example:

Test	Result
print(blackjack_hand_total([2, 3, 5]))      10
print(blackjack_hand_total([11, 5, 5]))     21
'''

def blackjack_hand_total(hand:list) -> int:

    asso = 0
    somma = 0

    for i in hand:
        
        somma += i

        if i == 11:
            asso += 1

        if somma > 21:
            somma -= 10
            asso -= 1
        
    return somma

	
print(blackjack_hand_total([2, 3, 5])) 	
print(blackjack_hand_total([11, 5, 5]))	
print(blackjack_hand_total([1, 10, 11]))
print(blackjack_hand_total([1, 10, 5]))
print(blackjack_hand_total([11, 5, 3]))
print(blackjack_hand_total([1, 11, 10]))