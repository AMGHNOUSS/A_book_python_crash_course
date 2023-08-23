class Restaurant:
    """ Class Restaurant define a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        """ Method __init__ to initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def  describe_restaurant(self):
        """ Print description of a restaurant"""
        print(f"The name of restaurant is: {self.restaurant_name}")
        print(f"The type of cuisine {self.cuisine_type}")
    
    def  open_restaurant(self):
        """Method printing a message open a restaurant"""
        print(f"The restaurant {self.restaurant_name} is openning!")