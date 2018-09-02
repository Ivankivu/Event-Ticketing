# user string input to search for
lines = []

user_input = input('Enter name:')

with open('ordinary.txt')as ordinary_file:
    lines = ordinary_file.readlines()
    for line in lines:
        if user_input == '':
            user_input = input('Enter name:')
        elif user_input.lower()in line.lower():
            print(line, 'ordinary ticket', end = '')
            break

with open('vip.txt')as vip_file:
    linez = vip_file.readlines()
    for line in linez:
        if user_input == '':
            user_input = input('Enter name:')
        elif user_input.lower()in line.lower():
            print(line, 'vip Ticket', end = '')
            break
    # if user_input != line:
    #     print ('Not registered')
