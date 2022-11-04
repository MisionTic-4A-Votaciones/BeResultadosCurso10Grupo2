from models import candidate


class PartyController:
    def __init__(self):
        """
        Party controller
        """
        print('Party controller')

    def index(self) -> dict:
        """
        method to get all parties
        :return: list
        """
        print('Get all')

    def show(self, id_: str) -> dict:
        """
        method to get a candidate by the id
        :param id_: candidate id
        :return: dict
        """
        print('Get by id')

    def create(self, party_: str) -> dict:
        """
        method to create a new party
        :param party_: dictionary with party info
        :return: dict
        """
        print('Create a party')

    def update(self, id_: str, party_: str) -> dict:
        """
        method to update party information by id
        :param id_: party id
        :param party_: dictionary with party info
        :return: dict
        """
        print('Update a party')

    def delete(self, id_: str) -> dict:
        """
        method to delete a pt by id
        :param id_: party id
        :return: str
        """
        print('Delete')
