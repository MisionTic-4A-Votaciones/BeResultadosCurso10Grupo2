from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:
    def __init__(self):
        """
        Party controller
        """
        print('Party controller')
        self.party_repository = PartyRepository()

    def index(self) -> dict:
        """
        method to get all parties
        :return: list
        """
        return self.party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        method to get a candidate by the id
        :param id_: candidate id
        :return: dict
        """
        return self.party_repository.find_by_id(id_)

    def create(self, party_: dict) -> dict:
        """
        method to create a new party
        :param party_: dictionary with party info
        :return: dict
        """
        print('Create a party')
        party = Party(party_)
        return self.party_repository.save(party)

    def update(self, id_: str, party_: dict) -> dict:
        """
        method to update party information by id
        :param id_: party id
        :param party_: dictionary with party info
        :return: dict
        """
        print('Update a party')
        party = Party(party_)
        return self.party_repository.update(id_, party)

    def delete(self, id_: str) -> dict:
        """
        method to delete a pt by id
        :param id_: party id
        :return: str
        """
        print('Delete')
        return self.party_repository.delete(id_)
