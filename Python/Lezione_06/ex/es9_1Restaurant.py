# 9-1. Restaurant

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name is: {self.restaurant_name}\nThe cuisine is: {self.cuisine_type}")
    
    def open_restaurant(self):
        print ("The restaurant is open!")

r0 = Restaurant("restaurant from your class", "Indian")

r0.describe_restaurant()
r0.open_restaurant()