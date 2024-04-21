from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_user_by_username, 
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


'''
Page/Action Routes
'''  

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')


@user_views.route('/signup', methods=['POST'])
def create_user_action():
    data = request.form
    user = get_user_by_username(data['username'])
    if user:
        flash(f"User {data['username']} already exists!")
        return redirect(url_for('user_views.get_signup_page'))
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))


'''
API Routes
'''

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)


@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})


@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')