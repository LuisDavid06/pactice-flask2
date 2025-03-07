from flask import Blueprint, render_template
from  todor.auth import login_required
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
@login_required
def index():
    return render_template('todo/index.html')

@bp.route('/create')
@login_required
def create():
    return 'Crear una tarea'