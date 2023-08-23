from users import User

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
