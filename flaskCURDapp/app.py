from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
  
  ################################

app = Flask(__name__)
app.secret_key = "sectretKey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/netflix.netflixData"
mongo = PyMongo(app)
   
   ###################

@app.route('/add',methods=['POST'])
def add_user():
    _json = request.get.json
    # _name = _json['name']
    # _email = _json['email']
    # _password = _json['password']
    _id = _json['id']
    _title = _json['title']
    _type = _json['type']
    _description = _json['description']
    _release_year = _json['release_year']
    _age_certification = _json['age_certification']
    _runtime = _json['runtime']
    _genres = _json['genres']
    _production_countries = _json['production_countries']
    _imbd_score = _json['imbd_score']

    # if _name and _email and _password and request.methods == 'POST':
    #     _hashed_password = generate_password_hash(_password)

    #     id = mongo.db.netflixData.inser({'name': _name, 'email': _email, 'pwd': _hashed_password})
    #     resp = jsonify("Data enter successfully")
    #     resp.status_code = 200
    #     return resp
    if _id and _title and _type and _description and _release_year and _age_certification and _runtime and _genres and _production_countries and _imbd_score and methods == 'POST':
        id = mongo.db.netflixData.insert({'id': _id, 'title': _title, 'type': _type, 'description': _description, 'release_year': _release_year, 'runtime': _runtime, 'genres': _genres, 'production_countries': _production_countries, 'imbd_score':_imbd_score})
        resp = jsonify("Data enterd successfully")
        resp.status_code=200
        return resp

    else:
        return not_found()

@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message ={
        'status': 404,
        'message': 'not_found' + request.url
    }
    resp = jsonify(message)
    resp.status_code =404
    return resp


   #################

if __name__ == '__main__':
    app.run(debug=True)

    #################
