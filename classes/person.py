from humans import Person, User, GuestList, EmptyNameException
import manage
from main.api.users import get_user, get_users, add_user, delete_user

person = Person ("black", "Ivan Kivumbi", "male", 26)

print(Person.description())

user = User(1, "kivumbi ivan","bunga-soya", 25, "Male")

print("user {} is {}, coming from {}, {} years old and a {}.".format(user.user_id, user.name, user.address, user.age, user.sex))

guestlist = GuestList()


saved_users = guestlist.get_users(1)

print(saved_users)