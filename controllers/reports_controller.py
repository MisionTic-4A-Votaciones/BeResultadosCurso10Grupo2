from repositories.reports_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_greatest_vote(self):
        return self.report_repository.get_greatest_vote()
