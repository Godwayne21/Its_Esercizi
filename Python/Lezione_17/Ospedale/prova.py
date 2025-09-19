from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura

d1 = Dottore("Lebron", "James","Medico Generale", 99.0)
d2 = Dottore("Stephen", "Curry","Pediatra", 95.0)

d1.doctorGreet()
d2.doctorGreet()