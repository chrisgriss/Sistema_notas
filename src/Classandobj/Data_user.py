from .User import Usuario
class Data:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if isinstance(user, Usuario):
            self.users.append(user)
            return True
        else:
            return False

    def get_users(self):
        return self.users
    
    def get_user(self, username):
        for user in self.users:
            if user.get_usuario() == username:
                return user
        return None

    def verify_user(self, username):
        for user in self.users:
            if user.get_usuario() == username:
                return True
        return False
    
    def verify_password(self, username, password):
        for user in self.users:
            if user.get_usuario() == username and user.get_password() == password:
                return True
        return False
    
    def verify_notas(self, username):
        for user in self.users:
            if user.get_usuario() == username:
                return user.exist_notas()
        return False

datos = Data()

def get_datos():
    return datos