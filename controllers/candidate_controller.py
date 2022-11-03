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
        data = {
            "marcadores": [
                {
                    "latitude": 40.416875,
                    "longitude": -3.703308,
                    "city": "Madrid",
                    "description": "Puerta del Sol"
                },
                {
                    "latitude": 40.417438,
                    "longitude": -3.693363,
                    "city": "Madrid",
                    "description": "Paseo del Prado"
                },
                {
                    "latitude": 40.407015,
                    "longitude": -3.691163,
                    "city": "Madrid",
                    "description": "Estación de Atocha"
                }
            ]
        }
        return [data]

    def show(self, id_: str) -> dict:
        """
        method to bring a candidate using id as a param
        :param id_:
        :return: dict
        """
        print('get one by id')
        candidate_ = {
            "_id": id_,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return candidate_

    def create(self, candidate_: dict) -> dict:
        """
        method to add a new candidate
        :param candidate_: dict with candidate info
        :return: dict
        """
        print('Create')
        candidate = Candidate(candidate_)
        return candidate.__dict__

    def update(self, id_: str, candidate_: str):
        """
        method to update a candidate info
        :param id_: candidate id
        :param candidate_: dict with candidate info
        :return: dict
        """
        print('Update')

    def delete(self, id_: str) -> str:
        """
        method to delete a candidate
        :param id_: Candidate id
        :return: str
        """
        print('Delete')
