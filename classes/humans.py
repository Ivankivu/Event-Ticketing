

class Person():
    def __init__(self, user_id, name, address, age, sex):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.age = age
        self.sex = sex

    def description(self):
        return "The person is a  {} with characteristics {}".format(self.user_id, self.name, self.address, 
                                                                    self.sex, self.age)

    def sound(self):
        return "{} user_id laughs like Hahaha  Hehehe".format(self.user_id)

class User():
    def __init__(self, user_id, name, address, age, sex):
        super().__init__(user_id, address, sex, age)
        self.user_id = user_id
    
    def clap(self):
        return "clap clap clap"
    
    def sound(self):
        return "arrrrh!"

class GuestList():
    def __init__(self, address, user_id, age, sex):
        super().__init__(address, user_id, age)
        self.sex = sex
    
    def talk(self):
        return "{} is made of more females than males".format(self.sex)
    
class EmptyNameException(Exception):

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors