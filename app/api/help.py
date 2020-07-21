from flask import url_for, jsonify
from app.api import bp


@bp.route('/help', methods=['GET'])
def help_():
    help_dict = {
        "User": {
            "create_user ['POST']": "users",
            "get_user ['GET']": "users/<id>",
            "get_users ['GET']": "users",
            "update_user ['PUT']": "users/<id>"
        },
        "Boards": {
            "create_board ['POST']": "boards",
            "get_board ['GET']": "boards/<registration_number>",
            "get_boards ['GET']": "boards",
            "update_board ['PUT']": "boards/<registration_number>"
        },
        "Directions": {
            "create_direction ['POST']": "directions",
            "get_direction ['GET']": "directions/<id>",
            "get_directions ['GET']": "directions",
            "update_direction ['PUT']": "directions/<id>"
        },        
        "Flights": {
            "create_flight ['POST']": "flights",
            "get_flight ['GET']": "flights/<id>",
            "get_flights ['GET']": "flights",
            "update_flight ['PUT']": "flights/<id>"
        },
        "Load files": {
            "download_file ['GET']": "download/<filename>",
            "upload_file ['POST']": "upload",
            "uploaded_files ['GET']": "uploaded_files"
        },
        "Manufacturers": {
            "create_manufacturer ['POST']": "manufacturers",
            "get_manufacturer ['GET']": "manufacturers/<id>",
            "get_manufacturers ['GET']": "manufacturers",
            "update_manufacturer ['PUT']": "manufacturers/<id>"
        },        
        "Models": {
            "create_model ['POST']": "models",
            "get_model ['GET']": "models/<id>",
            "get_models ['GET']": "models",
            "update_model ['PUT']": "models/<id>"
        },
        "Parameter values": {
            "create_parameter_value ['POST']": "parameter_values",
            "get_parameter_value ['GET']": "parameter_values/<id>",
            "get_parameter_values ['GET']": "parameter_values",
            "update_parameter_value ['PUT']": "parameter_values/<id>"
        },        
        "Parameters": {
            "create_parameter ['POST']": "parameters",
            "get_parameter ['GET']": "parameters/<id>",
            "get_parameters ['GET']": "parameters",
            "update_parameter ['PUT']": "parameters/<id>"
        },        
        "Phases of flight": {
            "create_phase_of_flight ['POST']": "phases_of_flight",
            "get_phase_of_flight ['GET']": "phases_of_flight/<id>",
            "get_phases_of_flight ['GET']": "phases_of_flight",
            "update_phase_of_flight ['PUT']": "phases_of_flight/<id>"
        }        
    }
    return jsonify(help_dict)
