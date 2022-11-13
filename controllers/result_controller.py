from models.table import Table
from models.result import Result
from models.candidate import Candidate
from repositories.table_repository import TableRepository
from repositories.result_repository import ResultRepository
from repositories.candidate_repository import CandidateRepository


class ResultController:
    # constructor
    def __init__(self):
        """
        Constructor of the VoteController class
        """
        print("Result controller")
        self.result_repository = ResultRepository()
        self.table_repository = TableRepository()
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """
        This method gets all the votes into the DB
        :return: Vote's list
        """
        print("Get all")
        return self.result_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.result_repository.find_by_id(id_)

    def get_by_table(self, table_id: str) -> list:

        return self.result_repository.get_candidates_in_table(table_id)

    def create(self, result_: dict, table_id: str, candidate_id: str) -> dict:
        """

        :param result_:
        :return:
        """
        result = Result(result_)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        result.table = table_obj
        result.candidate = candidate_obj
        return self.result_repository.save(result)

    def update(self, id_: str, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        print("Update by id")
        result = Result(result_)
        return self.result_repository.update(id_, result)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
        return self.result_repository.delete(id_)
