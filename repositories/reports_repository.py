from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository(Result)):
    def get_greatest_grade(self):
        query_aggregation = {
            "_id": "$table",
            "max": {"$max": "$votos_mujeres"},
            "doc": {"$first": "$$ROOT"}
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
    
    