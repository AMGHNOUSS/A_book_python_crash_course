class Restaurant:
    """ Class Restaurant define a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        """ Method __init__ to initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def  describe_restaurant(self):
        """ Print description of a restaurant"""
        print(f"The name of restaurant is: {self.restaurant_name}")
        print(f"The type of cuisine {self.cuisine_type}")
        print(f"The number of customers is : {self.number_served}")
    
    def  open_restaurant(self):
        """Method printing a message open a restaurant"""
        print(f"The restaurant {self.restaurant_name} is openning!")
    
    def set_number_served(self, n):
        """Set The number of customers that have been served"""
        self.number_served = n
    
    def increment_number_served(self, n):
        """Increment the numbers of customers."""
        self.number_served += n
restaurant = Restaurant('Friends', 'Italy')
restaurant.describe_restaurant()
print("--------------")
restaurant.number_served = 20
restaurant.describe_restaurant()
print("--------------")
restaurant.set_number_served(50)
restaurant.describe_restaurant()
print("--------------")
restaurant.increment_number_served(40)
restaurant.describe_restaurant()