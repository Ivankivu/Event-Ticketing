from flask import Flask, Request, jsonify, json

ivan = Flask(__name__)

users = [ {

        "user_id": 1,
        "Fullname": 'Ivan Kivumbi',
        "Age": 25},
        {

        "user_id": 2,
        "Fullname": 'Molly Namatovu',
        "Age": 22},
        {

        "user_id": 3,
        "Fullname": 'Tomusange Nkalubo',
        "Age": 20}]


@ivan.route('/', methods=['GET'])
def welcome():
    return jsonify({'message':'You are most welcome!'})

@ivan.route('/users', methods=['GET'])
def get_users():
    if users == []:
        return "Users not found", 404
        
    else:
        return jsonify({'users':users}), 200
        
    
if __name__ == '__main__':
    ivan.run(debug=True, port=5000)