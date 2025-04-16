import MIAW.tools.main as main
from services import db

def add():
    room_number = input('room_number: ')
    facility = input('facility: ')
    available = int(input('available: '))
    
    db.insert_item(room_number, facility, available)
    print(any)
    
def check():
    pass
    
def start():
    while True:
        menu = input('menu: 1. Booking rooms\n2. Checking rooms\n3. Back')
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
    
if __name__=='__main__':
    start()