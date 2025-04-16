from MIAW.tools.library import welcome_message, exit_program
from games import findingsluts
from MIAW.tools import Room

def menu():
    user_option = int(input(f'Menu:\n1. FindingSluts Games\n2. Room Booking\n3. Exit\n\nChoose any option: '))
    
    if user_option == 1:
        findingsluts.start()
    elif user_option == 2:
        Room.start()
    elif user_option == 3:
        exit_program()
    else:
        print('Option undefined!')

def main():
    welcome_message()
    menu()  
    
if __name__ == '__main__':
    main()