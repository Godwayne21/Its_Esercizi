# 9-4. Number Served

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f"The name is: {self.restaurant_name}\nThe cuisine is: {self.cuisine_type}")
    
    def open_restaurant(self) -> None:
        print ("The restaurant is open!")
    
    def number_served(x=0) -> None:
        print (x)
        return x

served = Restaurant

served.number_served()