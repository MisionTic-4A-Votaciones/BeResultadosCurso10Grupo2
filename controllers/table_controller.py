from models.table import Table


class TableController:

    def __int__(self):
        """
        Constructor of the tables
        """
        print("controller")

    def index(self) -> list:
        """

        :return:
        """
        print("Get all")

    def show(self, id_: str) -> dict:  # Or Table
        """

        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")

    def update(self, id_, table_: dict) -> dict:
        """
        
        :param id_:
        :param table_:
        :return:
        """
        print("Update")

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete")