from repositories.reports_repository import ReportsRepository


class ReportsController:
    def __init__(self):
        self.reports_repository = ReportsRepository()

    def get_greatest_grade(self):
        return self.reports_repository.get_greatest_grade()