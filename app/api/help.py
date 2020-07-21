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
        }

    }
    return jsonify(help_dict)
