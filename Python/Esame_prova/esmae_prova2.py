class Ticket():

    ticket_id: str
    movie:str
    seat:str
    is_booked:bool

    def __init__(self, ticket_id:str, movie:str, seat:str)->None:
        self.ticket_id = ticket_id
        self.movie = movie
        self.seat = seat
        self.is_booked = False
    
    def book(self,)->