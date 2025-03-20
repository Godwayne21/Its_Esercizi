from persona2 import Persona

gr:Persona = Persona()

gr.displayData()

print("-------------")

#imposta il nome della persona gr
gr.setName("Godwayne")
gr.displayData()

#imposto il cognome della persona gr
gr.setLastName("Rasalan")
gr.displayData()

#imposto l'età della persona gr
gr.setAge(24)
gr.displayData()

print("-------------")

print(gr.getName(), gr.getLastName(), gr.getAge())