from repositories.


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_greatest_result(self):
        return self.report_repository.
