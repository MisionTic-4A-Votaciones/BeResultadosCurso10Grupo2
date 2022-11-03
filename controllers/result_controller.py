from models.result import Result


class ResultController:
    # Constructor
    def __int__(self):
        """
        Constructor of the results
        """
        print("controller")

    # get ALL results
    def index(self) -> list:
        """

        :return:
        """
        print("Get all")
        data = {
            "_id": "abc456",
            "mesa#": "14",
            "parti_id": "df65"
        }
        return [data]

    # get ONE result by ID
    def show(self, id_: str) -> dict:  # Or Result
        """

        :param id_:
        :return:
        """
        print("Show by id")
        data = {
            "_id": id_,
            "mesa#": "18",
            "parti_id": "abc324"
        }
        return data

    # INSERT result
    def create(self, result_: dict) -> dict:
        """

        :param result_:
        :return:
        """
        print("Insert")
        result = Result(result_)
        return result.__dict__

    # UPDATE result
    def update(self, id_, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        print("Update")
        data = result_
        data['_id'] = id_
        result = Result(result_)
        return result.__dict__

    # DELETE result
    def delete(self, id_: str) -> dict:
        """
        
        :param id_:
        :return:
        """
        print("Delete" + id_)
        return {"Delete count": 1}
    
        

        