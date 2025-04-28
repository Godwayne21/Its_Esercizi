from formaGenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")
    
    def draw(self)->None: