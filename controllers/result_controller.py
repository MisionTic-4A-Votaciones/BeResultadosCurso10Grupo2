

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

    # get ONE result by ID
    def show(self, id_: str) -> dict:  # Or Result
        """

        :param id_:
        :return:
        """
        print("Show by id")

    # INSERT result
    def create(self, result_: dict) -> dict:
        """

        :param result_:
        :return:
        """
        print("Insert")

    # UPDATE result
    def update(self, id_, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        print("Update")

    # DELETE result
    def delete(self, id_: str) -> dict:
        """
        
        :param id_:
        :return:
        """
        print("Delete")
        

        