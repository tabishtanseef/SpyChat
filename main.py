from spy_details import spy_salutation, spy_name, spy_rating, spy_age
print 'Hello'
print 'Let\'s get started'

STATUS_MESSAGE = ['Status1', 'I m in class', 'spy is enjoying ']

def add_status(status_message):

    if status_message != None:
        print 'Your Current status is' + status_message
    else:
        print 'You don\'t have a status '

    ques = raw_input('Do you want to select from the old status? Y\N ')
    if ques.upper() == 'N':
        new_status = raw_input('Enter Your new status: ')
        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)
    elif ques.upper()== 'Y':
        item_position = 1
        for messages in STATUS_MESSAGE:
            print str(item_position) + '. ' + messages
            item_position = item_position + 1
        message_selection = input('Choose from the above status ')
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]
            return updated_status_message


def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    status_message = None
    while show_menu:
        menu_choice = input('What do you want to do? \n 1. Add a status. \n 2. Exit Application')
        if menu_choice==1:
            print 'Update Your status'
        elif menu_choice==2:
            show_menu = False





question = raw_input('Are you an existing user? Y\N ')
if (question == 'Y'):
    print 'okay'
    start_chat(spy_name,spy_age,spy_rating)
else:
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        #Start writing from here now. See how this is under the if statement?
        print 'Welcome ' + spy_name + '. Glad to have you back with us.'
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")
        spy_name = spy_salutation + " " + spy_name
        print 'Alright ' + spy_name + '. I\'d like to know a little bit more about you before we proceed...'
        spy_age = input('What is your age?')
        if spy_age> 12 and spy_age< 50:
            spy_rating = input('What is your spy rating?')
            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

            start_chat(spy_name, spy_age, spy_rating)
        else:
            print 'Your age is not correct to become a spy'

    else:
        print "Please enter a valid name"