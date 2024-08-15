from website.errors import bp
from flask import render_template

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404