from models.candidate import Candidate
from repositories.candidate_repository import CandidateRepository


class CandidateController:
    def __init__(self):
        """
        Candidates constructor
        """
        print("Candidate controller")
        self.candidate_repository = CandidateRepository()

    def index(self):
        """
        method to get all candidates
        :return: list
        """
        print("get all")
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        method to bring a candidate using id as a param
        :param id_:
        :return: dict
        """
        print('get one by id')
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """
        method to add a new candidate
        :param candidate_: dict with candidate info
        :return: dict
        """
        print('Create')
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: str):
        """
        method to update a candidate info
        :param id_: candidate id
        :param candidate_: dict with candidate info
        :return: dict
        """
        candidate = Candidate(candidate_)
        return self.update(id_, candidate)

    def delete(self, id_: str) -> dict:
        """
        method to delete a candidate
        :param id_: Candidate id
        :return: str
        """
        print('Delete' + id_)
        return self.candidate_repository.delete(id_)
