import postcopg2

class DatabaseConnection:
    def __init__(self):

        try:
            self.connection = psycopg2.connect(
            """
            dbname = 'addDB' user ='ivan' password = 'password'
            host = 'localhost' port = '5432'
            """
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('\n\nConnected to Database\n\n')
        
        except expression as e:
            print(e.message)
            print('failed to connect to db')

    def createUser():
       