from flask import Blueprint, request, jsonify, session
#from src.Classandobj.Data_user import get_datos
from Classandobj.Data_user import get_datos

login_bp = Blueprint('login', __name__)


username = ''
def get_username():
    global username
    return username

def set_username(user):
    global username
    username = user

@login_bp.route('/login', methods=['POST'])
def login():
    datos = request.json
    username = datos.get('username')
    password = datos.get('password')

    dat = get_datos()

    if dat.verify_user(username):
        if dat.verify_password(username, password):
            set_username(username)
            return jsonify({'message': 'Login exitoso'}), 200
        else:
            return jsonify({'error': 'Contraseña incorrecta'}), 401
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@login_bp.route('/logout', methods=['DELETE'])
def logout():
    global username
    if username is not '':
        set_username('')
        return jsonify({'message': 'Logout exitoso'}), 200
    else:
        return jsonify({'error': 'No hay sesión activa'}), 400