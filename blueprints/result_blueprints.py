from flask import Blueprint
from flask import request  # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.result_controller import ResultController

result_blueprints = Blueprint('result_blueprints', __name__)
result_controller = ResultController()


@result_blueprints.route("/result/all", methods=['GET'])
def get_all_results():
    response = result_controller.index()
    return response, 200


@result_blueprints.route("/result/<string:id_>", methods=['GET'])
def get_result_by_id(id_):
    response = result_controller.show(id_)
    return response, 200


@result_blueprints.route("/result/table/<string:table_id>", methods=['GET'])
def get_result_by_table(table_id):
    response = result_controller.get_by_table(table_id)
    return response, 200


@result_blueprints.route("/result/insert/table/<string:table_id>/candidate/<string:candidate_id>", methods=['POST'])
def insert_result(table_id, candidate_id):
    result = request.get_json()
    response = result_controller.create(result, table_id, candidate_id)
    return response, 201


@result_blueprints.route("/result/update/<string:id_>", methods=['PATCH'])
def update_result(id_):
    result = request.get_json()
    response = result_controller.update(id_, result)
    return response, 201


@result_blueprints.route("/result/delete/<string:id_>", methods=['DELETE'])
def delete_result(id_):
    response = result_controller.delete(id_)
    return response, 204
