from jsonpickle import encode
from flask import request, Response, Blueprint
from flask_httpauth import HTTPBasicAuth
from .user import User

api_user = Blueprint('api_user',__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'python' and password == 'python':
            return True
        else:
            return False
    return False

@api_user.route('/user', methods=['GET'])
@auth.login_required
def get_user():
    return Response(
        response = encode(User.items),
        status = 200,
        mimetype = "application/json")

@api_user.route('/user/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth.login_required
def user_by_id(id):
    if request.method == 'GET':
        item = User.find_item(id)
        if item == None:
            return Response(
                response = f"User with id={id} not found!",
                status = 404)
        else:
            return Response(
                response = encode(item),
                status = 200,
                mimetype = "application/json")

    if request.method == 'POST':
        try:
            User.add_item(request.form.to_dict())
            return Response(
                response = 'OK', 
                status = 200)
        except:
            return Response(
                response = f"User with id={id} exists!",
                status = 404)

    if request.method == 'PUT':
        try:
            item = User.update_item(id, request.form.to_dict())
            return Response(
                response = encode(item),
                status = 200,
                mimetype = "application/json")
        except:
            return Response(
                response = f"User with id={id} not found!",
                status = 404)

    if request.method == 'DELETE':
        try:
            item = User.delete_item(id)
            return Response(
                response = 'OK', 
                status = 200)
        except:
            return Response(
                response = f"User with id={id} not found!",
                status = 404)
