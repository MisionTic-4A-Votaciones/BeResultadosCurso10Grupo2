from models.result import Result
from repositories.result_repository import ResultRepository


class ResultController:

    def __init__(self):
        """
        Constructor of the results
        """
        print("ResultController")
        self.result_repository = ResultRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("Get all")
        return self.result_repository.find_all()

    def show(self, id_: str) -> dict:  # Or Result
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.result_repository.find_by_id(id_)

    def create(self, result_: dict) -> dict:
        """

        :param result_:
        :return:
        """
        print("Insert")
        result = Result(result_)
        return self.result_repository.save(result)

    def update(self, id_, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        result = Result(result_)
        return self.update(id_, result)

    def delete(self, id_: str) -> dict:
        """
        
        :param id_:
        :return:
        """
        print("Delete" + id_)
        return self.result_repository.delete(id_)
