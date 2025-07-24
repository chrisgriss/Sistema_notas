from flask import Blueprint, jsonify, session, request
from Classandobj.Data_user import get_datos
#from src.Classandobj.Data_user import get_datos
from users.Backend.users.login import get_username

registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/registro', methods=['POST'])
def registro():
    imports = request.json

    nota = imports.get('nota')

    username = get_username()
    datos = get_datos()
    usuario = datos.get_user(username)

    if usuario is None:
        return jsonify({'message':'Usuario no encontrado'}), 404
    else:
        if vf_nota(nota):
                usuario.add_nota(nota)
                return jsonify({'message':'Nota ingresada correctamente'}), 200
        else:
            return jsonify({'message':'La nota debe de estar entre 0 a 100'}), 400

def vf_nota(nota):
    if nota < 0 or nota > 100:
        return False
    return True

@registro_bp.route('/mostrar_notas', methods=['GET'])
def mostrar_notas():
    username = get_username()
    datos = get_datos()
    usuario = datos.get_user(username)

    if usuario is None:
        return jsonify({'error':'Usuario no encontrado'}), 404
    else:
        notas = usuario.get_notas()
        promedio_nota = float(promedio(notas))
        return jsonify({'notas': notas, 'promedio': promedio_nota}), 200
def promedio(notas):
    cantidad = len(notas)
    if cantidad == 0:
        return 0
    suma = sum(notas)
    return suma / cantidad