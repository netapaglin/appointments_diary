from datetime import date, datetime, time, timedelta
import resources
import ui
import re

def main():
    run_diary = True
    diary = {}
    rooms = resources.create_rooms()
    persons = resources.create_persons()
    insert_from_file(diary, rooms, persons)
    while run_diary:
        action = ui.print_menu()
        if action == 1: #create
 #           insert_meet(diary, meet1, rooms, persons)
 #           insert_meet(diary, meet2, rooms, persons)
  #          insert_meet(diary, meet3, rooms, persons)
            print('diary', diary)
            meet = create_meet(rooms, persons)
            insert_meet(diary, meet, rooms, persons)
    #       print('diary', diary)
    #       print('rooms', rooms)
    #       print('persons', persons)
        elif action == 2: #search
            meet = search_general(diary)
            if meet != -1:
                ui.print_meet(meet)
        elif action == 3: #delete
            delete_general(diary, rooms, persons)
        elif action == 4: #print
            print_meetings(diary)
        elif action == 5: #exit
            save_to_file(diary)
            print('Exit')
            run_diary = False
        else:
            print('Wrong input')


#def load_file(_diary, _rooms, _persons):

def extract_letters(line):
    letters = re.findall(r'[a-zA-Z]+', line)
    return letters

def insert_from_file(_diary, _rooms, _persons):
    f = open("text.txt", 'r')
    line = f.readline()
    while line:
        words = line.split()
        letters = extract_letters(line)
        lst = []
        for i in range(1, (len(letters))):
            lst.append(letters[i])
        new_meet = {
            'name': words[0],
            'date': words[1],
            'start': words[2],
            'end': words[3],
            'room': words[4],
            'participants': lst}
        insert_meet(_diary, new_meet, _rooms, _persons)
        print('lst', lst)
        print('new_meet', new_meet)
        line = f.readline()
    f.close()
def save_to_file(_diary):
    try:
        f = open("text.txt", "w+")
        for value in _diary.values():
            for dictionary in value:
                for v in dictionary.values():
                    print(v, end=" ", file=f)
                print(file=f)
        f.flush()
        f.close()
    except FileNotFoundError:
        print("FileNotFoundError exeption")
        return
    except:
        print("Something went wrong")
        return


def if_time_date_valid(_date, _start, _end):
    if _date.weekday() == 4 or _date.weekday() == 5:
        ui.print_date_error()
        return False
    if _start < time(9,0):
        ui.print_early_error()
        return False
    if _end > time(18,0):
        ui.print_late_error()
        return False
    if _start > _end:
        ui.print_time_error()
        return False
    if _date < datetime.now().date():
        ui.print_old_date_error()
        return False
    timedelta_start = str(_start)
    shours, sminutes, sseconds = map(int, timedelta_start.split(':'))
    start_timedelta = timedelta(hours=shours, minutes=sminutes, seconds=sseconds)
    timedelta_end = str(_end)
    ehours, eminutes, eseconds = map(int, timedelta_end.split(':'))
    end_timedelta = timedelta(hours=ehours, minutes=eminutes, seconds=eseconds)
    if (end_timedelta - start_timedelta) <= timedelta(minutes=15):
        ui.print_tooshort_error()
        return False
    return True

def create_meet(_rooms , _persons):
    try:
        valid_room = False
        meeting_name, the_date, start, end = ui.print_create_name_date()
        if if_time_date_valid(the_date, start, end) == False:
            return
        while not valid_room:
            room = resources.get_room_number()
            if room == -1:
                return
            print('room - ', room)
            if resources.room_check_available(_rooms, room, the_date, start, end):
                valid_room = True
        lst = check_members(_persons, the_date, start, end)
        new_meet = {
            'name': meeting_name,
            'date': the_date,
            'start': start,
            'end': end,
            'room': room,
            'participants': lst}
        return new_meet
    except:
        print('Something went wrong, please try again ')
        return None


def check_members(_persons, _date, _start, _end):
    run_check = 1
    members_list = []
    while run_check:
        name = ui.create_participant()
        if resources.person_check_available(_persons, name, _date, _start, _end) == False:
            continue
        members_list.append(name)
        if ui.if_create_more_participant() == 0:
            break
    return members_list
def insert_meet(_diary, _meet, _rooms , _persons):
    try:
        insert_to_diary(_diary, _meet)
        resources.insert_to_rooms(_rooms, _meet)
        resources.insert_all_participants(_persons, _meet)
    except:
        ui.print_error()
        return

def print_meetings(_diary):
    choosen_print = ui.print_choose_method()
    if choosen_print == 1: #print all meetings
        for lst in _diary.values():
            for meet in lst:
                ui.print_meet(meet)
    elif choosen_print == 2: #print by dates
        print('Under construction')
    elif choosen_print == 3: # print by member
        print('Under construction')
    else:
        print('Wrong input')
def delete_general(_diary, _rooms, _persons):
    date_meet, start_meet, room_number = ui.print_meet_to_search_delete()
    found_meet = search_meet(_diary, date_meet, start_meet, room_number)
    meet = delete_meet(_diary, found_meet, _rooms , _persons)
    return meet

def delete_meet(_diary, _meet, _rooms , _persons):
    try:
        meet_date = _meet['date']
        start = _meet['start']
        room_number = _meet['room']
        diary_delete_meet(_diary, meet_date, start, room_number)
        resources.room_delete_meet(_rooms, _meet)
        resources.delete_all_participants_meets(_persons, _meet)
    except:
        ui.print_error()
        return

def insert_to_diary(_diary , _meet):
    date = _meet['date']
    meet_list=[]
    if _diary.get(date) is None:
        _diary[date] = meet_list
    _diary[date].append(_meet)

def search_general(_diary):
    date_meet, start_meet, room_number = ui.print_meet_to_search_delete()
    meet = search_meet(_diary, date_meet, start_meet, room_number)
    return meet
def search_meet(_diary, _date, _start, _room_number):
    if _diary.get(_date) is None:
        print('_date', _date)
        print('meeting not found')
        return -1
    for meet in _diary[_date]:
        if meet['start'] == _start and meet['room'] == _room_number:
            print('meet found')
            return meet
        else:
            print('2 meeting not found')
            return -1
def diary_delete_meet(_diary, _date, _start, _room_number):
    meet = search_meet(_diary, _date, _start, _room_number)
    if meet == -1:
        print('meet not found')
        return -1
    _diary[_date].remove(meet)
    if not _diary[_date]:
        _diary.pop(_date)

# tests

#insert_to_diary(diary , new_meet)
#insert_to_diary(diary , meet1)
#insert_to_diary(diary , meet2)
#print(diary)

curr_date = date(2023, 10, 1)
curr_time = time(10, 30)
#search_result = search_meet(diary, curr_date , curr_time, 1)
#ui.print_meet(search_result)
#print('search', search_result)

#my_date = date(2025,7,12)
#specific_time = datetime.combine(datetime.today().date(), time(10, 30))

#print(specific_time.time())


meet1 = {
    'name': 'greater',
    'date': date(2023, 10, 1),
    'start': time(10, 30),
    'end': time(11, 30),
    'room': 2,
    'participants': ['Roni', 'Adi', 'Noga']}

meet3 = {
    'name': 'hi',
    'date': date(2023, 10, 1),
    'start': time(10, 30),
    'end': time(11, 30),
    'room': 3,
    'participants': ['Neta', 'Eli']}

meet2 = {
    'name': 'hellow',
    'date': date(2023, 10, 3),
    'start': time(10, 30),
    'end': time(11, 30),
    'room': 2,
    'participants': ['Dorit', 'Uri']}





if __name__ == '__main__':
    main()


