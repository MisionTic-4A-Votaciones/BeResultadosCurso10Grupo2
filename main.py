import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidate_blueprints import candidate_blueprints
from blueprints.party_blueprints import party_blueprints
from blueprints.result_blueprints import result_blueprints
from blueprints.table_blueprints import table_blueprints

regisApp = Flask(__name__)
cors = CORS(regisApp)

regisApp.register_blueprint(party_blueprints)
regisApp.register_blueprint(candidate_blueprints)
regisApp.register_blueprint(result_blueprints)
regisApp.register_blueprint(table_blueprints)


@regisApp.route("/", methods=['GET'])

def home():
    response={"message": "Welcome to Registraduria MINTIC"}
    return jsonify(response)


#=========Config and Execution code===============
def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(regisApp, host=data_config.get('url-backend'), port=data_config.get('port'))

