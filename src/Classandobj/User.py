class Usuario:
    def __init__(self, usuario, nombre, email, password):
        self.usuario = usuario
        self.nombre = nombre
        self.email = email
        self.password = password

    def get_usuario(self):
        return self.usuario
    
    def get_nombre(self):
        return self.nombre
    
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email

    def __str__(self):
        return f'Usuario: {self.usuario}, Nombre: {self.nombre}, Email: {self.email}'

class Profesor(Usuario):
    def __init__(self, usuario, nombre, email, password, asignatura):
        super().__init__(usuario, nombre, email, password)
        self.asignatura = asignatura
        self.notas = []

    def get_asignatura(self):
        return self.asignatura
    
    def add_nota(self, nota):
        self.notas.append(nota)
    
    def delete_nota(self, nota):
        if nota in self.notas:
            self.notas.remove(nota)
            return True
        return False
    
    def get_notas(self):
        return self.notas

    def exist_notas(self):
        if len(self.notas) > 0:
            return True
        return False

    def __str__(self):
        return f'{super().__str__()}, Asignatura: {self.asignatura}'