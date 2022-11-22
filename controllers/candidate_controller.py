from models.candidate import Candidate
from models.party import Party
from repositories.candidate_repository import CandidateRepository
from repositories.party_repository import PartyRepository


class CandidateController:
    # constructor
    def __init__(self):
        """
        Constructor of the CandidateController class
        """
        print("Candidate controller")
        self.candidate_repository = CandidateRepository()
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        This method gets all the candidates into the DB
        :return: Candidate's list
        """
        print("Get all")
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """

        print("Insert")
        candidate = Candidate(candidate_)

        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("Update by id")
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
        return self.candidate_repository.delete(id_)
    
    def party_assign(self, candidate_id: str, party_id: str) -> dict:
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        party_dict = self.party_repository.find_by_id(party_id)
        party_obj = Party(party_dict)
        candidate_obj.party = party_obj
        return self.candidate_repository.save(candidate_obj)

