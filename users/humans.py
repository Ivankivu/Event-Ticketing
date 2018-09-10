from flask import Flask, Blueprint
man = Flask(__name__)

people = Blueprint("GuestList", __name__)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "My name is {}, ia am {} years old".format(self.name, self.age)

    def sound(self):
        return "{} laughs like this  -> Hahaha  Hehehe".format(self.name)

class User():

    def __init__(self, user_id, name, age):
        
        super().__init__(user_id,name, age)
        self.user_id = user_id
        self.name = name
        self.age = age
      
    
    def id(self):
        return self.user_id
    

class GuestList():
    def __init__(self, user_id, name, age):
        super().__init__(user_id, name)
        self.name = name
        self.user_id = user_id
        self.api = []

    def check_list(self):
        api = self.api
        return api

    def check_user(self, user_id):
        return "{} belongs to".format(self.user_id)

    def check_user_exists(self, id):
        return self.api.__contains__(id)

    def add_a_user(self,name,user_id):
       pass

    def get_users(self):
        if (self.api) == []:
            return "no user found"
        return self.api

    def get_a_user(self, user_id):
        return self.api
        
class EmptyNameException(Exception):

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors