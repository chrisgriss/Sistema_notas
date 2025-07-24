from flask import Blueprint, request, jsonify
#from src.Classandobj.Data_user import get_datos
#from src.Classandobj.User import Profesor

from Classandobj.Data_user import get_datos
from Classandobj.User import Profesor

signin_bp = Blueprint('signin', __name__)

@signin_bp.route('/signin', methods=['POST'])
def signin():
    datos = request.json
    username = datos.get('username')
    name = datos.get('name')
    password = datos.get('password')
    email = datos.get('email')
    asignatura = datos.get('asignatura')

    datos = get_datos()
    
    if not username or not name or not password:
        return jsonify({'error': 'No hay datos'}), 400
    else:
        if vf_password(password):
            if datos.verify_user(username):
                return jsonify({'error': 'El usuario ya existe'}), 400
            else:
                profesor = Profesor(username, name, email, password, asignatura)
                if datos.add_user(profesor):
                    return jsonify({'message': 'Usuario creado exitosamente'}), 201
        else:
            return jsonify({'error': 'La contraseña debe tener al menos 8 caracteres, una mayúscula y un dígito'}), 400

def vf_password(password):
    mays = False
    digit = False

    if len(password) < 8:
        return False
    
    for char in password:
        if char.isdigit():
            digit = True
        if char.isupper():
            mays = True

    if mays and digit:
        return True
        
    return False
    