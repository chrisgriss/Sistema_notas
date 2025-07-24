from flask import Blueprint, request, jsonify, session
#from src.Classandobj.Data_user import get_datos
from Classandobj.Data_user import get_datos
from users.Backend.users.login import get_username

home_bp = Blueprint('home', __name__)

@home_bp.route('/home', methods=['GET'])
def home():
    username = get_username()
    user_data = get_datos()

    if user_data.verify_notas(username):
        return jsonify({
            'message': f'Bienvenido {username}, tienes notas registradas.',
            'username': username,
            'asignatura': get_asignatura(username)
        }), 200
    else:
        return jsonify({
            'message': f'Bienvenido {username}, no tienes notas registradas.',
            'username': username,
            'asignatura': get_asignatura(username)
        }), 200
    
def get_asignatura(username):
    user_data = get_datos()

    for user in user_data.get_users():
        if user.get_usuario() == username:
            return user.get_asignatura()
        
    return None