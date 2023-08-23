class User:
    """Class user define a user"""
    def __init__(self, first_name, last_name, age, city):
        """Method __init__ initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def describe_user(self):
        """Decribe Information of user"""
        print(f"The user {self.last_name} {self.first_name} has {self.age} years old, he was born in {self.city}")
    
    def greet_user(self):
        """Gretting a user"""
        print(f"Hello, {self.last_name} {self.first_name}!")