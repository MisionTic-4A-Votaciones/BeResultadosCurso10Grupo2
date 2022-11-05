from models.table import Table
from repositories.table_repository import TableRepository


class TableController:

    def __int__(self):
        """
        Constructor of the results
        """
        print("TableController")
        self.table_repository = TableRepository

    def index(self) -> list:
        """

        :return:
        """
        print("Get all")
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:  # Or Result
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

    def update(self, id_, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        table = Table(table_)
        return self.update(id_, table)
