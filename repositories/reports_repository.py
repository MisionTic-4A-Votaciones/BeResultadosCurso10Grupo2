from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Result]):
	def get_greatest_vote(self):
		query_aggregation = {
			"$group": {
			"_id": "$table",
			"max": {"$max": "$total_votos"},
			"doc": {"$first": "$$ROOT"}
			}
		}
		pipeline = [query_aggregation]
		return self.query_aggregation(pipeline)


	def get_results_by_candidate(self):
		query_lookup = {
			"$lookup": {
			"from": "candidate",
  			"localField": "candidate.$id",
  			"foreignField": "_id",
  			"as": "details"
			}
		}

		query_unwind = {
			"$unwind": "$details"
		}

		query_group = {
			"$group": {
				"_id": "$details",
			  	"votos": {"$sum": "$votos"}
			}
		}

		qury_add_fields = {
			"$addFields": {
				"nombre": "$_id.nombre",
   				"apellido": "$_id.apellido",
   				"_id": "$_id._id",
   				"partido": "$_id.party"
			}
		}

		query_sort = {
			"$sort": {
				"votos": -1
			}
		}

		pipeline = [query_lookup, query_unwind, query_group, qury_add_fields, query_sort]
		return self.query_aggregation(pipeline)


