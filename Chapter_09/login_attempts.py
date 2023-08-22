class User:
    """Class user define a user"""
    def __init__(self, first_name, last_name, age, city):
        """Method __init__ initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0
    
    def describe_user(self):
        """Decribe Information of user"""
        print(f"The user {self.last_name} {self.first_name} has {self.age} years old, he was born in {self.city}")
    
    def greet_user(self):
        """Gretting a user"""
        print(f"Hello, {self.last_name} {self.first_name}!")
    
    def increment_login_attempts(self):
        """Increments the value of login_attemps"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0

user1 = User('Redouane', 'AMGHNOUSS', 21, 'Laayoune')

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)