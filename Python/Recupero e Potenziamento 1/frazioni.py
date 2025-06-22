class Frazioni:

    _numeratore:int
    _denominatore:int

    def __init__(self, numeratore:int, denominatore:int)->None:

        self._numeratore = numeratore
        self. _denominatore = denominatore
    
    def set_Numeratore (self, numeratore:int)->int:

        if isinstance (numeratore,int):
            self._numeratore = numeratore
        else:
            self._numeratore = 13
    
    def set_Denominatore (self, denominatore:int)->int:
        
        if isinstance (denominatore, int) and denominatore != 0:
            self._denominatore = denominatore
        
        else:
            self._denominatore = 5
    
    def get_Numeratore (self)->int:
        return self._numeratore
    
    def get_Denominatore (self)->int:
        return self._denominatore
    
    def __str__(self):
        
        return f"{self._numeratore}/{self._denominatore}"
    
    def value (self):

        return round ((self._numeratore / self._denominatore),3)
    

    def mcd(x:int, y:int)->int:

        if x > y:
            while y!= 0:
                x, y = y, x % y

            return abs(x)
        
        elif x < y:
            while x!= 0:
                y, x = x, y % x
            
            return abs(y)
        
        else:
            return 1


n