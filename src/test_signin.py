import unittest
from main import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.cliente = self.app.test_client()

    def test_signin(self):
        datos = {
            "username" : "p_test001",
            "name" : "profesor_test",
            "password" : "Prueba1234",
            "email" : "test@example",
            "asignatura" : "Matematica Intermedia 1" 
        }

        response = self.cliente.post('/api/signin', json=datos)
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.get_json(), {'message' : 'Usuario creado exitosamente'})

    def test_signin_f(self):
        datos = {
            "username" : "p_test002",
            "name" : "profesor_test",
        }
        response = self.cliente.post('/api/signin',json = datos)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error':'No hay datos'})

    def test_signin_password(self):
        datos = {
            "username" : "p_test003",
            "name" : "profesor_test",
            "password" : "pruebaxxx",
            "email" : "test@example",
            "asignatura" : "Matematica Intermedia 1"
        }
        response = self.cliente.post('/api/signin',json = datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'error': 'La contraseña debe tener al menos 8 caracteres, una mayúscula y un dígito'})

if __name__ == '__main__':
    unittest.main()