 
def users():
        # user string input to search for
        global lines
        global user_input
        lines = []
        user_input = input('Enter name:')
        
        if user_input == '':
            user_input = input('Enter name:')
        else:
            if __name__ == '__main__':
                paid_tickets(user_input)

def paid_tickets(user_input):
        with open('ordinary.txt')as ordinary_file:
            lines = ordinary_file.readlines()
            for line in lines:
                if user_input.lower()in line.lower():
                    print(line, 'ordinary ticket', end = '')
                   

        with open('vip.txt')as vip_file:
            linez = vip_file.readlines()
            for line in linez:
                if user_input == '':
                    user_input = input('Enter name:')
                elif user_input.lower()in line.lower():
                    print(line, 'vip Ticket', end = '')
                    
            # if user_input != line:
            #     print ('Not registered')

if __name__ == '__main__':
    users()