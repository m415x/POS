from flask import Blueprint

superadmin_bp = Blueprint('super_admin', __name__, template_folder='templates')

from . import routes