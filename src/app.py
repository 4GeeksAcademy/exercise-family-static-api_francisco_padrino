"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['POST','GET'])
def listFamily():
    # This is how you can use the Family datastructure by calling its methods
    if (request.method == 'GET'):
        members = jackson_family.get_all_members()
        if (len(list(members)) > 0):
            response = jsonify(members)
            response.status_code = 200
            return response
        else:
            response = jsonify({"Estado":"Error", "mensaje":"Error, no se ha encontrado familia"})
            response.status_code = 400 
            return response
        return response    
    elif (request.method == 'POST'):
        age= request.json["age"]
        first_name = request.json["first_name"]
        lucky_numbers = request.json["lucky_numbers"]
        member1 = {"age":age,"first_name":first_name,"id":jackson_family._generate_id(),"last_name":jackson_family._paslastname(),"lucky_numbers":lucky_numbers }
        members = jackson_family.add_member(member1)
        response = jsonify(members)
        response.status_code = 200
        return response

        
@app.route("/members/<int:id>", methods=[ 'GET','DELETE'])
def Listfamilyid(id):
    if (request.method == 'GET'):
        members = jackson_family.get_member(id)
        if (len(list(members)) > 0):
            response = jsonify(members)
            response.status_code = 200
            return response
        else:
            response = jsonify({"Estado":"Error", "mensaje":"Error, no se ha encontrado familiar"})
            response.status_code = 400 
            return response
    elif (request.method == 'DELETE'):
         members = jackson_family.delete_member(id)
         response = jsonify(members)
         response.status_code = 200
         return response
    else:
        response = jsonify({"Estado":"Error", "mensaje":"Error, Metodo no permitido"})
        response.status_code = 400 
        return response
    

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
