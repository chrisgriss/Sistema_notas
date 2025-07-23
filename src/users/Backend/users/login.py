from flask import Blueprint, request, jsonify, session
from Classandobj.Data_user import get_datos

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    datos = request.json
    username = datos.get('username')
    password = datos.get('password')

    dat = get_datos()

    if dat.verify_user(username):
        if dat.verify_password(username, password):
            session['username'] = username
            session['logged_in'] = True
            return jsonify({'message': 'Login exitoso'}), 200
        else:
            return jsonify({'error': 'Contraseña incorrecta'}), 401
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@login_bp.route('/logout', methods=['DELETE'])
def logout():
    if 'username' in session and session.get('logged_in'):
        session.pop('username', None)
        session['logged_in'] = False
        return jsonify({'message': 'Logout exitoso'}), 200
    else:
        return jsonify({'error': 'No hay sesión activa'}), 400

@login_bp.route('/session', methods=['GET'])
def check_session():
    if 'username' in session and session.get('logged_in'):
        return jsonify({'logged_in': True, 'username': session['username']}), 200
    return jsonify({'logged_in': False}), 401