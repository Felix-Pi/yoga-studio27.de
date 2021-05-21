from flask import render_template
from sqlalchemy import desc

from app.routes.home import bp


@bp.route('/')
def home():
    templateData = {
        'user': None,
    }

    return render_template('home/home.html', **templateData, title=('Home'))


@bp.route('/timetable')
def timetable():
    templateData = {
        'user': None,
    }

    return render_template('timetable/base.html', **templateData, title=('Stundenplan'))

@bp.route('/pricing')
def pricing():
    templateData = {
        'user': None,
    }

    return render_template('pricing/base.html', **templateData, title=('Kursgebühren'))


@bp.route('/studio')
def studio():
    templateData = {
        'user': None,
    }

    return render_template('studio/base.html', **templateData, title=('Das Studio'))

@bp.route('/contact')
def contact():
    templateData = {
        'user': None,
    }

    return render_template('contact/base.html', **templateData, title=('Das Studio'))
