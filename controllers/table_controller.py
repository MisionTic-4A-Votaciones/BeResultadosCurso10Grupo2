from models.table import Table
from models.party import Party
from repositories.table_repository import TableRepository
from repositories.party_repository import PartyRepository


class TableController:
    # constructor
    def __init__(self):
        """
        Constructor of the TableController class
        """
        print("Table controller")
        self.table_repository = TableRepository()
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        This method gets all the tables into the DB
        :return: Table's list
        """
        print("Get all")
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.table_repository.find_by_id(id_)

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """

        print("Insert")
        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update by id")
        table = Table(table_)
        return self.table_repository.update(id_, table)

    def delete(self, id_: str, ) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
        return self.table_repository.delete(id_)

    def party_assign(self, table_id: str, party_id: str) -> dict:
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        party_dict = self.paty_repository.find_by_id(party_id)
        party_obj = Party(party_dict)
        table_obj.party = party_obj
        return self.table_repository.save(table_obj)
