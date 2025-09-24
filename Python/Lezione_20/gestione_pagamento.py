class Pagamento():

    __payment__:float

    def __init__(self)->None:
        pass
    
    def setPayment(self, payment:float)->None:
        self.__payment__ = payment
    
    def getPayment(self)->float:
        return self.__payment__
    

    def dettagliPagamento(self)->str:
        print (f"Importo del pagamento {self.getPayment(): .2f}")
    
class PagamentoContanti(Pagamento):

    def __init__(self,payment:float)->None:
        super().__init__()
        self.__payment__ = int(round(payment * 100))
        self.banconote = {}

    def dettagliPagamento(self)->str:

        return super().self.dettagliPagamento() + "in contanti"
    
    def inPezziDa(self) -> None:
        tagli = [
            (50000, "banconota da 500 euro"),
            (20000, "banconota da 200 euro"),
            (10000, "banconota da 100 euro"),
            (5000, "banconota da 50 euro"),
            (2000, "banconota da 20 euro"),
            (1000, "banconota da 10 euro"),
            (500,  "banconota da 5 euro"),
            (200,  "moneta da 2 euro"),
            (100,  "moneta da 1 euro"),
            (50,   "moneta da 0.50 euro"),
            (20,   "moneta da 0.20 euro"),
            (10,   "moneta da 0.10 euro"),
            (5,    "moneta da 0.05 euro"),
            (2,    "moneta da 0.02 euro"),
            (1,    "moneta da 0.01 euro")
        ]

        for valore, descrizione in tagli:
            while self.__payment__ >= valore:
                self.__payment__ -= valore
                if descrizione in self.banconote:
                    self.banconote[descrizione] += 1
                else:
                    self.banconote[descrizione] = 1
        
        risultati = []

        for key,value in self.banconote.items():

            if value > 0:
                risultati.append(f"{value} {key}")
        
        return risultati
    
    