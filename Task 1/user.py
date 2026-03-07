class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_user_id(self):
        return self.__user_id
    
    def get_name(self):
        return self.__name
    
    def is_admin(self):
        return False
    
class Admin(User):
    def is_admin(self):
        return True