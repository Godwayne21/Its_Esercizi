from film import Film
from movie_genre import Azione
from movie_genre import Commedia
from movie_genre import Drama

class Noleggio():
    
    __film_list__:list
    __rented_film__:dict

    def __init__(self, film_list:list[Film])->None:
        self.__film_list__ = film_list[Film]
        self.__rented_film__ = {}
    
    def isAvaible(self, film:Film)->bool:
        if film in self.__film_list__:
            print (f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        
        else:
            print (f"Il film scelto è disponibile: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film:Film, id_client)->None:

        if film in self.__film_list__:
             
             print (f"Il cliente {id_client:int} ha noleggiato {film.getTitle()}!")
             self.__film_list__.remove(film)
        
             if id_client not in self.__rented_film__:
                
                client_film = []
                self.__rented_film__[id_client] = client_film
            
             else:
                self.__rented_film__[id_client] = client_film.append(film)
        
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")

    def giveBack(self, film, clientID, days)->int:
        