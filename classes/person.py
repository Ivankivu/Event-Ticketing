from humans import Person, User, GuestList, EmptyNameException

person = Person("Ivan Kivumbi","male",26)

print(Person.details())

user = User("kivumbi ivan","bunga-soya",25, "Male")

print("This  is {},coming from {}, {} years old and a {}.".format(user.name, user.address, user.age, user.sex))

guestlist = GuestList()


added_user = guesslist.find_user_by_email(1)

print(added_user)