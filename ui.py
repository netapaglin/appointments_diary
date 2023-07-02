from datetime import date,datetime, time
def print_menu():
    try:
        print('****** DIARY ******')
        print('1. Create new meeting')
        print('2. Search meet')
        print('3. Delete meet')
        print('4. Print meet')
        print('5. Exit')
        choosen_num = int(input('Please choose an action...'))
        return choosen_num
    except ValueError:
        print('Wrong input')
        print_menu()

def print_choose_method():
    try:
        print('1. Print all meetings')
        print('2. Print by dates')
        print('3. Print by member')
        choosen_num = int(input('Please choose an action...'))
        return choosen_num
    except ValueError:
        print('Wrong input')
        print_menu()
def print_meet_to_search_delete():
    try:
        date_meet = input("Enter the date (in YYYY-MM-DD format): ")
        start_meet = input("Enter the time to start the meet (in HH:MM format): ")
        room_number = int(input('Choose room number: '))
        the_date = datetime.strptime(date_meet, "%Y-%m-%d").date()
        start = datetime.strptime(start_meet, "%H:%M").time()
        return the_date, start, room_number
    except ValueError:
        print("Invalid Input")
        print_meet_to_search_delete()

def print_create_name_date():
    try:
        meeting_name = input(' write meeting name: ')
        date_meet = input("Enter the date (in YYYY-MM-DD format): ")
        start_meet = input("Enter the time to start the meet (in HH:MM format): ")
        end_meet = input("Enter the time to end the meet (in HH:MM format): ")
        the_date = datetime.strptime(date_meet, "%Y-%m-%d").date()
        start = datetime.strptime(start_meet, "%H:%M").time()
        end = datetime.strptime(end_meet, "%H:%M").time()
 #       print("meeting_name:", meeting_name)
 #       print("date:", the_date)
 #       print("Time start:", start)
  #      print("Time end:", end)
        return meeting_name, the_date, start, end
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format and date in YYYY-MM-DD format.")



def create_participant():
    try:
        human = input('Who will participant in the meeting? ')
        return human
    except ValueError:
        print("Invalid input")
        create_participant()

def if_create_more_participant():
    try:
        print('Would you like to invite more participants?')
        more = int(input(' 1 - Yes   , 0 - No '))
        if more != 0 and more != 1:
            print("please choose zero or one")
            if_create_more_participant()
        return more
    except ValueError:
        print("Invalid input.")
        if_create_more_participant()

def print_meet(_meet):
    print('*' * 25)
    print('Subject - ', _meet['name'])
    print(_meet['date'])
    print(_meet['start'], ' - ', _meet['end'])
    print('Room number - ', _meet['room'])
    print('Room participants - ')
    for human in _meet['participants']:
        print(human, end='  ')
    print()
    print('*' * 25)

def print_early_error():
    print('It is too early, the meet can start from 9:00')

def print_late_error():
    print('It is too late, the meet can not end after 18:00')

def print_tooshort_error():
    print('It is too short, the meet can not be shorter than 15 minutes')

def print_time_error():
    print('The start time have to be before the end time')

def print_date_error():
    print('You can not have meetings on weekend')

def print_old_date_error():
    print('This date is in the past')

def print_overlap_error():
    print('The room is occupied')

def print_person_overlap_error():
    print('This person can not join the meeting')

def print_error():
    print('Sorry, something went wrong')