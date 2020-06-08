from flask import render_template

from app.models import User
from . import home as home_blueprint


@home_blueprint.route('/all/users', methods=['GET'])
def all_users():
    """
    List all Users
    """
    all_users = User.query.all()
    return render_template('home/home.html', users=all_users, title="Users")