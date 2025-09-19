class Film():

    __id__: int
    __title__: str

    def __init__(self,id:int,title:str)->None:
        self.__id__ = id
        self.__title__ = title
    
    def setID (self,id)->None:

        self.__id__ = id
    
    def setTitle(self,title:str)->None:

        self.__title__ = title
    
    def getID(self)->int:
        return self.__id__
    
    def getTitle(self)->str:
        return self.__title__
    
    def isEqual(self, otherFilm)->bool:
        self.otherFilm = otherFilm
        
        if self.__id__ == otherFilm:
            return True
        
        else:
            return False
    