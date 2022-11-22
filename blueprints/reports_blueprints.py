from flask import Blueprint
from controllers.reports_controller import ReportController


reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportController()


@reports_blueprints.route("/reports/highest_vote", methods=['GET'])
def get_highest_vote():
    response = reports_controller.get_greatest_vote()
    return response, 200


@reports_blueprints.route("/reports/results_by_candidate", methods=['GET'])
def get_results_by_candidate():
    response = reports_controller.get_results_by_candidate()
    return response, 200


