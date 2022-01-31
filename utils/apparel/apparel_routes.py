from jsonpickle import encode
from flask import request, Response, Blueprint
from .apparel import Apparel

api_apparel = Blueprint('api_apparel',__name__)

@api_apparel.route('/apparel', methods=['GET'])
def get_apparel():
    return Response(
        response = encode(Apparel.items),
        status = 200,
        mimetype = "application/json")

@api_apparel.route('/apparel/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def apparel_by_id(id):
    if request.method == 'GET':
        item = Apparel.find_item(id)
        if item == None:
            return Response(
                response = f"Apparel with id={id} not found!",
                status = 404)
        else:
            return Response(
                response = encode(item),
                status = 200,
                mimetype = "application/json")

    if request.method == 'POST':
        try:
            Apparel.add_item(request.form.to_dict())
            return Response(
                response = 'OK', 
                status = 200)
        except:
            return Response(
                response = f"Apparel with id={id} exists!",
                status = 404)

    if request.method == 'PUT':
        try:
            item = Apparel.update_item(id, request.form.to_dict())
            return Response(
                response = encode(item),
                status = 200,
                mimetype = "application/json")
        except:
            return Response(
                response = f"Apparel with id={id} not found!",
                status = 404)

    if request.method == 'DELETE':
        try:
            item = Apparel.delete_item(id)
            return Response(
                response = 'OK', 
                status = 200)
        except:
            return Response(
                response = f"Apparel with id={id} not found!",
                status = 404)
