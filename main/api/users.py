from flask import Flask, request, jsonify, json, Blueprint
users = Blueprint("users", __name__)

ivan = Flask(__name__)


api = []

@users.route("/", methods=["GET"])
def welcome():
    return jsonify({"message":"You are most welcome!"})


@users.route("/api/get-users", methods=["GET"])
def get_users():
    if api == []:
        return "users not found", 404
        
    else:
        return jsonify({"api":api}), 200

@users.route("/api/add-user", methods=["POST"])
def add_user():
    user = {    "user_id" : request.json["user_id"],
                "Age" :     request.json["Age"],
                "name":     request.json["name"]
        }
    for user_id in user:
        if user["user_id"] == user_id:
            return "User already exists"
        
    api.append(user)
    return jsonify({"user":user}), 200 
    

@users.route("/api/get-users/<string:user_id>", methods=["GET"])
def get_user(user_id):

    use = [user for user in api if user["user_id"] == user_id]
    return jsonify({"use": use[0]}), 200

@users.route("/api/delete", methods=["DELETE"])
def delete_user(user_id):

    for user in api:
        if user["user_id"] == user_id:
            del user
    return "{} is deleted.".format(["name"])
                
