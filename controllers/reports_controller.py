from repositories.reports_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.reports_repository = ReportRepository()

    def get_greatest_vote(self):
        return self.reports_repository.get_greatest_vote()

    def get_results_by_candidate(self):
        return self.reports_repository.get_results_by_candidate()
