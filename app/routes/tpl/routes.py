from flask import render_template
from sqlalchemy import desc

from app.routes.tpl import bp


@bp.route('/index')
def index():
    templateData = {
        'user': None,
    }

    return render_template('pages/index.html', **templateData, title=('Home'))


@bp.route('/generic')
def generic():
    templateData = {
        'user': None,
    }

    return render_template('pages/generic.html', **templateData, title=('Home'))


@bp.route('/elements')
def elements():
    templateData = {
        'user': None,
    }

    return render_template('pages/elements.html', **templateData, title=('Home'))
