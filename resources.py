from datetime import date, datetime, time
import ui
def create_rooms():
    rooms_dict = {}
    return rooms_dict

def insert_to_rooms(_rooms , _meet):
    room_number = _meet['room']
    room_list = []
    room_tuple = (_meet['date'], _meet['start'], _meet['end'])
    if _rooms.get(room_number) is None:
        _rooms[room_number] = room_list
    _rooms[room_number].append(room_tuple)

def room_search_meet(_rooms , _meet):
    meet_date = _meet['date']
    meet_start = _meet['start']
    room_num = _meet['room']
    if _rooms.get(room_num) is None:
        print('room not found')
        return -1
    for meet in _rooms[room_num]:
        if meet[0] == meet_date and meet[1] == meet_start:
            print('room meet found')
            return meet
        else:
            print('room meeting not found')
            return -1

def room_delete_meet(_rooms , _meet):
    room_number = _meet['room']
    meet_time = room_search_meet(_rooms , _meet)
    if meet_time == -1:
        print('meet not found')
        return -1
    _rooms[room_number].remove(meet_time)
    if not _rooms[room_number]:
        _rooms.pop(room_number)

def room_check_available(_rooms, _room_number, _date, _start, _end):
    if _room_number in _rooms.keys():
        for item in _rooms[_room_number]:
            if item[0] == _date and (item[1] < _start < item[2] or item[1] < _end< item[2]):
                ui.print_overlap_error()
                return False
            if item[0] == _date and (_start < item[1] < _end or _start < item[2] < _end):
                ui.print_overlap_error()
                return False
    return True

def get_room_number():
    try:
        valid_room_number = False
        room_number = None
        room_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while valid_room_number == False:
            room_number = int(input('Choose room number: '))
            if room_number in room_list:
                # valid_room_number = True
                print('NumBer', room_number)
                return room_number
            else:
                print('Invalid room number')
    except ValueError:
        print("Invalid input")
        return -1
        # create_room()

def create_persons():
    person_dict = {}
    return person_dict

def insert_to_persons(_persons ,_meet, _name):
    persons_list = []
    persons_tuple = (_meet['date'], _meet['start'], _meet['end'])
    if _persons.get(_name) is None:
        _persons[_name] = persons_list
    _persons[_name].append(persons_tuple)

def insert_all_participants(_persons ,_meet):
    for human in _meet['participants']:
        insert_to_persons(_persons, _meet, human)

def participants_search_meet(_persons , _meet , _name):
    meet_date = _meet['date']
    meet_start = _meet['start']
    if _persons.get(_name) is None:
        print('Person not found')
        return -1
    for meet in _persons[_name]:
        if meet[0] == meet_date and meet[1] == meet_start:
            print('person meet found')
            return meet
        else:
            print('person meeting not found')
            return -1

def participants_delete_meet(_persons , _meet , _name):
    meet_time = participants_search_meet(_persons , _meet , _name)
    if meet_time == -1:
        print('person meet not found')
        return -1
    _persons[_name].remove(meet_time)
    if not _persons[_name]:
        _persons.pop(_name)

def delete_all_participants_meets(_persons ,_meet):
    for human in _meet['participants']:
        participants_delete_meet(_persons, _meet, human)

def person_check_available(_persons, _name, _date, _start, _end):
    if _name in _persons.keys():
        for item in _persons[_name]:
            if item[0] == _date and (item[1] < _start < item[2] or item[1] < _end< item[2]):
                ui.print_person_overlap_error()
                return False
            if item[0] == _date and (_start < item[1] < _end or _start < item[2] < _end):
                ui.print_person_overlap_error()
                return False
    return True

meet1 = {
    'name': 'greater',
    'date': date(2023, 10, 1),
    'start': time(10, 30),
    'end': time(11, 30),
    'room': 2,
    'participants': ['Roni', 'Adi', 'Noga']}

meet2 = {
    'name': 'grandmizer',
    'date': date(2023, 10, 1),
    'start': time(10, 30),
    'end': time(11, 30),
    'room': 4,
    'participants': ['Eli', 'Neta', 'Noga']}




# tests
def print_persons(_persons):
    print()

#rooms_dict = create_rooms()
#insert_to_rooms(rooms_dict , meet1)
#insert_to_rooms(rooms_dict , meet2)
#print(rooms_dict)

#persons = create_persons()
#insert_all_participants(persons, meet2)
#print(persons)