from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:
    # constructor
    def __init__(self):
        """
        Constructor of the PoliticalPartyController class
        """
        print("Party controller")
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        This method gets all the political parties into the DB
        :return: Political party's list
        """
        print("Get all")
        return self.party_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.party_repository.find_by_id(id_)

    def create(self, party_: dict) -> dict:
        """

        :param party_:
        :return:
        """

        print("Insert")
        party = Party(party_)
        return self.party_repository.save(party)

    def update(self, id_: str, party_: dict) -> dict:
        """

        :param id_:
        :param party_:
        :return:
        """
        print("Update by id")
        party = Party(party_)
        return self.party_repository.update(id_, party)

    def delete(self, id_: str, ) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
        return self.party_repository.delete(id_)
