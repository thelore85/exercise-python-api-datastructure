"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os  
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


'''
DONE  -  /members  GET - return all the jackson_family
DONE  -  /members  POST - add a family member + return the updated member list
DONE  -  /members/<int:id>  GET - return the selected member
/members/<int:id>  DELETE - delete the selected memebr
'''

# /members  GET - return all the jackson_family
@app.route('/members/', methods=['GET', 'POST'])
def handle_hello():
    response_body = {}

    if request.method == 'GET':
        members = jackson_family.get_all_members()

        if members:
            response_body['message'] = 'family member list'
            response_body['result'] = members
            return response_body, 200

        response_body['error'] = 'Error: no members list found in DB'
        return response_body, 500
    
    if request.method == 'POST':
        data = request.json
        jackson_family.add_member(data)
        response_body['message'] = 'New member added'
        response_body['result'] = jackson_family.get_all_members()

        return response_body, 200



@app.route('/members/<int:id>', methods=['GET'])
def handle_member(id):

    response_body = {}
    
    if request.method == 'GET':
        response_body['message'] = 'Selected user'
        response_body['result'] = jackson_family.get_member(id)
        return response_body, 200
    
    response_body['error'] = 'something gose wrong'
    return response_body, 500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
