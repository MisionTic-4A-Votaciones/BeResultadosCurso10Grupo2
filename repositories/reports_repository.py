from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ResultRepository(InterfaceRepository(Result)):
	def get_greatest_vote(self):
		query_agregation = {
			" ": " "
		}
	pipeline = [query_agregation]
	return self.query_agregation(pipeline)