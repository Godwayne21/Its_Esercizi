class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool = False)->None:

        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    
    def rent(self)->None:

        if self.is_rented:
            print (f"Il film '{self.title}' è già noleggiato.")
        
        else:
            self.is_rented = True
    
    def return_movie(self)->None:

        if not self.is_rented:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
        
        else:
            self.is_rented = False

class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]=None)->None:
        
        self.customer_id = customer_id
        self.name = name
        if rented_movies is not None:
            self.rented_movies = rented_movies
        else:
            self.rented_movies = []
    
    def rent_movie(self, movie: Movie)->None:

            if movie in self.rented_movies or movie.is_rented:
                print (f"Il film '{movie.title}' è stato noleggiato da questo cliente.")
            else:
                movie.is_rented = True
                self.rented_movies.append(movie)
    
    def return_movie(self, movie: Movie)->None:

        if movie in self.rented_movies:
            movie.is_rented = False
            self.rented_movies.remove(movie)
        
        else:
            print (f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer])-> None:

        self.movies = movies if movies is not None else {}
        self.customers = customers if customers is not None else {}

    def add_movie(self, movie_id: str, title: str, director: str)->None:

        if movie_id not in self.movies:

            self.movies [movie_id] = Movie[movie_id,title,director]
        
        else:
            print (f"Il film con ID '{movie_id}' esiste già.")