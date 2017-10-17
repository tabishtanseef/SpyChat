from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime
print 'Hello'
print 'Let\'s get started'

STATUS_MESSAGE = ['Status', 'I m in class', 'spy is enjoying ']

friends=[]

def add_status(current_status_message):

    if current_status_message != None:
        print 'Your Current status is ' + current_status_message
    else:
        print 'You don\'t have a status '

    ques = raw_input('Do you want to select from the old status? Y\N ')

    if ques.upper() == 'N':
        new_status = raw_input('Enter Your new status: ')

        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)
            return new_status

    elif ques.upper()== 'Y':

        item_position = 1

        for messages in STATUS_MESSAGE:
            print str(item_position) + '. ' + messages
            item_position = item_position + 1

        message_selection = input('Choose from the above status ')

        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]
            return updated_status_message
        else:
            print 'You dont have a status at this Number'
    else:
        print 'The option you choose is not valid. Either enter Y or N'


def add_friend():
    new_friend ={
        'name' : '',
        'salutation' : '',
        'age' : 0,
        'rating' : 0.0,
        'chats' : []
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_friend():
  item_number = 1

  for friend in friends:
    print '%d. %s' % (item_number, friend['name'])

    item_number = item_number + 1

  friend_choice = input("Choose from your friends")
  friend_choice_position = friend_choice - 1
  return friend_choice_position

def send_message():
    friend_choice = select_friend()
    original_image = raw_input("what is your original image? ")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say? ")
    text = Steganography.encode(original_image, output_path, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"

def read_message():
    sender = select_friend()
    output_path = raw_input("What is the output path? ")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your secret message is " + secret_text
    print "Your secret message has been saved!"

def start_chat(spy):

    show_menu = True

    current_status_message = None

    while show_menu:
        menu_choice = input('What do you want to do? \n 1. Add a status. \n 2. Add a friend. \n 3. Send Message \n 4. Read Message\n 5.Exit Application')
        if menu_choice==1:
            print 'Update Your status'
            current_status_message = add_status(current_status_message)
            if current_status_message:
                print 'Your Updated status message is ' + current_status_message
        elif menu_choice==2:
            number_of_friends = add_friend()
            print 'you have %d friends ' % (number_of_friends)
        elif menu_choice==3:
            send_message()
        elif menu_choice==4:
            read_message()
        else:
            show_menu = False





question = raw_input('Are you an existing user? Y\N ')
if (question == 'Y'):
    print 'okay'
    start_chat(spy)
else:
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy['name']) > 0:
        #Start writing from here now. See how this is under the if statement?
        print 'Welcome ' + spy['name'] + '. Glad to have you back with us.'
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")
        spy['name'] = spy['salutation'] + ' ' +spy['name']
        print 'Alright ' + spy['name'] + '. I\'d like to know a little bit more about you before we proceed...'
        spy['age'] = input("What is your age?")
        if spy['age']> 12 and spy['age']< 50:
            spy['rating'] = input('What is your spy rating?')
            if spy['rating'] > 4.5:
                print 'Great ace!'
            elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                print 'You are one of the good ones.'
            elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"

            start_chat(spy)
        else:
            print 'Your age is not correct to become a spy'

    else:
        print "Please enter a valid name"