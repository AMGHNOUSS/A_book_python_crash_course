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

class Admin(User):
    """Class Admin define a kind of user"""
    def __init__(self, first_name, last_name, age, city):
        """Add attribute privileges"""
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()
    
    
class Privileges:
    """Class Privileges define one attribute"""

    def __init__(self):
        """Method init define attribute privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display privileges to administator"""
        print(f"\t{self.privileges[0]} \n\t{self.privileges[1]} \n\t{self.privileges[2]}" )


admin = Admin('Redouane', 'AMGHNOUSS', 21, 'Laayoune')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()