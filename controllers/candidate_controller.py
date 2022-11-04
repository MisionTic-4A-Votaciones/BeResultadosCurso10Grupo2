from models.candidate import Candidate


class CandidateController:
    def __init__(self):
        """
        Candidates constructor
        """

    def index(self):
        """
        method to get all candidates
        :return: list
        """
        print("get all")

    def show(self, id_: str) -> dict:
        """
        method to bring a candidate using id as a param
        :param id_:
        :return: dict
        """
        print('get one by id')

    def create(self, candidate_: dict) -> dict:
        """
        method to add a new candidate
        :param candidate_: dict with candidate info
        :return: dict
        """
        print('Create')

    def update(self, id_: str, candidate_: str):
        """
        method to update a candidate info
        :param id_: candidate id
        :param candidate_: dict with candidate info
        :return: dict
        """
        print('Update')
        data = candidate_
        data['_id'] = id_
        student = Candidate(candidate_)
        return student.__dict__

    def delete(self, id_: str) -> dict:
        """
        method to delete a candidate
        :param id_: Candidate id
        :return: str
        """
        print('Delete')
