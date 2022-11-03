from flask import Blueprint
from flask import request

from controllers.party_controller import PartyController

party_blueprints = Blueprint('party_blueprints', __name__)
party_controller = PartyController()


@party_blueprints.route('/party/all', methods=['GET'])
def get_all_parties():
    """
    to bring all parties
    :return: list
    """
    response = party_controller.index()
    return response, 200


@party_blueprints.route('/party/<string:id_>', methods=['GET'])
def get_party_by_id(id_):
    """
    to bring a party given its id
    :param id_: party id
    :return: dict
    """
    response = party_controller.show(id_)
    return response, 200


@party_blueprints.route('/party/create', methods=['POST'])
def insert_party():
    """
    to create a new party
    :return: dict
    """
    party = request.get_json()
    response = party_controller.create(party)
    return response, 201


@party_blueprints.route('/party/update/<string:id_>', methods=['PATCH'])
def update_party(id_):
    """
    to update a party
    :param id_: party id
    :return: dict
    """
    party = request.get_json()
    response = party_controller.update(id_, party)


@party_blueprints.route('/party/delete/<string:id_>', methods=['DELETE'])
def delete_party(id_):
    """
    to delete a party
    :param id_: party id
    :return: str
    """
    response = party_controller.delete(id_)
    return response, 204



