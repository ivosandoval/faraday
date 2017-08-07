from flask import jsonify, session, Blueprint, current_app

session_api = Blueprint('session_api', __name__)

@session_api.route('/session')
def session_info():
    user = current_app.user_datastore.get_user(session['user_id'])
    return jsonify(user.get_security_payload())
