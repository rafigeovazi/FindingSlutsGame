import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    style = "=" * len(PC_NAME)
    print(style)
    print(f"{PC_NAME}")
    print(style)

def exit_program():
    print('This PC will blow up in💣:')
    sleep(1)
    print('10')
    sleep(1)
    print('9')
    sleep(1)
    print('8')
    sleep(1)
    print('7')
    sleep(1)
    print('6')
    sleep(1)
    print('5')
    sleep(1)
    print('4')
    sleep(1)
    print('3😦')
    sleep(1)
    print('2🤢')
    sleep(1)
    print('1☠️')
    sleep(1)
    print('DUUAARRR!!!!💥💥 imut😜')
    
if __name__=='__main__':
    welcome_message()
    exit_program()