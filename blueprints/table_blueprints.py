from flask import Blueprint
from flask import request # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.table_controller import TableController

table_blueprints = Blueprint('table_blueprints', __name__)
table_controller = TableController()


@table_blueprints.route("/table/all", methods=['GET'])
def get_all_table():
    response = table_controller.index()
    return response, 200


@table_blueprints.route("/table/<string:id_>", methods=['GET'])
def get_table_by_id(id_):
    response = table_controller.show(id_)
    return response, 200


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_table():
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprints.route("/table/update/<string:id_>", methods=['PATCH'])
def update_table(id_):
    table = request.get_json()
    response = table_controller.update(id_, table)
    return response, 201


@table_blueprints.route("/table/<string:table_id>/party/<string:party_id>", methods=['PUT'])
def assign_party(table_id, party_id):
    response = table_controller.party_assign(table_id, party_id)
    return response, 201


@table_blueprints.route("/table/delete/<string:id_>", methods=['DELETE'])
def delete_table(id_):
    response = table_controller.delete(id_)
    return response, 204
