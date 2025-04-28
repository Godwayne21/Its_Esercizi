from persona2 import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona
p:Persona = Persona("Godwayne", "Rasalan", 24)

#visualizzare le informazioni dell'oggetto p
print(p)

# creare un oggetto et della classe Alieno
et:Alieno = Alieno("James")

#visualizzare le informazioni dell'oggetto et
print(et)

# l'opggetto p invochi il metodo speak()
p.speak()