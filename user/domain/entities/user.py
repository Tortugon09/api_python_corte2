class User:
    def __init__(self, name, email, password, user_id=None): 
        self.name = name
        self.email = email
        self.password = password
        self.id = user_id  

    def check_password(self, password):
        return self.password == password
    