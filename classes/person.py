from humans import Person, User, GuestList, EmptyNameException

Person = Person("Haruna","+256775185123","har.mullah@gmail.com","Engineer")

print(Person.details())

user = User("kivumbi ivan","bunga-soya",25, "Male")

print("This  is {},coming from {}, {} years old and a {}.".format(user.name, user.address, user.age,\
  user.sex))

guesslist = GuestList()

guesslist.add_user(AppUsers(1, "ibn yusuf", "user@email.com"))
# guesslist.add_user(AppUsers("Doreen", "doreen@email.com"))
# guesslist.add_user(AppUsers("mark", "markn@email.com"))

added_user = guesslist.find_user_by_email(1)

print(added_user)