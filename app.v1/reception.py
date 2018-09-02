#user string input to search for 
lines = []
user_input = input('Enter name:')

empty = ''
with open ('ordinary.txt') as ordinary_file:
    lines = ordinary_file.readlines()
for line in lines:
        if user_input =='':
            user_input = input('Enter name:')
             
for line in lines:
        if user_input.lower() in line.lower():
            print (line,'ordinary ticket')
            break
          
with open ('vip.txt') as vip_file:           
    
        linez = vip_file.readlines()
        for line in linez:
            if user_input =='':
                user_input = input('Enter name:')
                
for line in linez:
        if user_input.lower() in line.lower():
            print (line, 'vip ticket')
            break

        
    



if user_input != line:
        print ('Not registered', end = '')


    




    # for file_input in ordinary_file:
    #     if user_input is empty:
    #         user_input = input('Enter name:')
    #     else:

    #         if user_input.lower() in file_input.lower():
    #             print (file_input, 'ordinary ticket')
    # else:
    #     if user_input is not file_input:
    #         print ('Not registered')
    
    # ordinary_file.close()

    # for file_input in vip_file: 
    #     if user_input.lower() in file_input.lower():
    #         print (file_input, 'vip ticket')
    # else:
    #     if user_input is not file_input:
    #         print ('Not registered')
                
    # vip_file.close()
