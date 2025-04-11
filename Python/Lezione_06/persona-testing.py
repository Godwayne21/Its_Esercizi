# dal file persona.py importa la classe Persona
from persona import Persona 

gr:Persona = Persona("Godwayne","Rasalan",24)

print(gr)

print(gr.name, gr.last_name, gr.age)

# sfrutto la funzione displayData della classe Persona per visualizzare in output i dati relativi alla persona gr
gr.displayData()