from flask import Blueprint
# from src.note_log.backend.note_log.home import home_bp
# from src.note_log.backend.note_log.registro_notas import registro_bp
# from src.users.Backend.users.login import login_bp
# from src.users.Backend.users.signin import signin_bp
from note_log.backend.note_log.home import home_bp
from note_log.backend.note_log.registro_notas import registro_bp
from users.Backend.users.login import login_bp
from users.Backend.users.signin import signin_bp


urls_bp = Blueprint('urls', __name__)
urls_bp.register_blueprint(home_bp)
urls_bp.register_blueprint(registro_bp)
urls_bp.register_blueprint(login_bp)
urls_bp.register_blueprint(signin_bp)