from humans import Person, User, GuestList, EmptyNameException
import manage
from main.api.users import get_user, get_users, add_user, delete_user

person = Person ("Ivan Kivumbi", 26)

print(Person.description())

user = User(1, "kivumbi ivan", 25)

print("user {} is {}, and {} years old.".format(user.user_id, user.name, user.age))

guestlist = get_users()

print(guestlist)