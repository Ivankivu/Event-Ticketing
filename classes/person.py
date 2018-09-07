from humans import Person, User, GuestList, EmptyNameException
import manage
from main.api.users import get_user, get_users, add_user, delete_user

person = Person("Ivan Kivumbi","male",26)

print(Person.details())

user = User("kivumbi ivan","bunga-soya", 25, "Male")

print("This  is {},coming from {}, {} years old and a {}.".format(user.name, user.address, user.age, user.sex))

guestlist = GuestList()


saved_users = guestlist.get_users(1)

print(saved_users)