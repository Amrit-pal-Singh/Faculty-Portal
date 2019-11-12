import datetime
from dateutil import parser
from infrastructure.switchlang import switch
import services.data_service as svc
import program
import infrastructure.state as state
from colorama import Fore
import infrastructure.state as state



def run():
    print('************* Welcome Professor ************* ')
    print()

    show_commands()

    while True:
        action = get_action()
        with switch(action) as s:
            s.case('c', create_account)
            s.case('l', log_into_account)
            s.case('y', view_your_profile)
            s.case('e', edit_your_profile)            
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.default(unknown_command)

        state.reload_account()

        if action:
            print()

        if s.result == 'change_mode':
            return

def create_account():
    print(' ****************** REGISTER **************** ')

    name = input('What is your name? ')
    email = input('What is your email? ').strip().lower()

    old_account = svc.find_account_by_email(email)
    if old_account:
        error_msg(f"ERROR: Account with email {email} already exists.")
        return


    print('What is your Department ? Choose')
    choice = int(input('''
    1. Computer Science
    2. Mechanical
    3. Chemical
    4. Electrical
    5. Math
    6. Biology
    7. Physics
    8. Humanities? '''))
    Department = ''
    if choice == 1: Department = 'CSE'
    elif choice == 2: Department = 'MEC'
    elif choice == 3: Department = 'CHE'
    elif choice == 4: Department = 'ELE'
    elif choice == 5: Department = 'MAT'
    elif choice == 6: Department = 'BIO'
    elif choice == 7: Department = 'PHY'
    elif choice == 8: Department = 'HUM'
 
    publications = []
    grants = []
    awards = []
    teachings = []
    check = input('Want to add publications? [y/n]').lower().startswith('y')
    while check:
        pub = input()
        publications.append(pub)
        yy = input('Wanna Add more? [y/n]').lower().startswith('y')
        if yy is not True:
            break
    check = input('Got some Grants? [y/n]').lower().startswith('y')
    while check:
        grnt = input()
        grants.append(grnt)
        yy = input('Got some more? [y/n]').lower().startswith('y')
        if yy is not True:
            break
    check = input('Won any Award? [y/n]').lower().startswith('y')
    while check:
        awd = input()
        awards.append(awd)
        yy = input('Got some more? [y/n]').lower().startswith('y')
        if yy is not True:
            break
    check = input('You teach AnyThing? [y/n]').lower().startswith('y')
    while check:
        tch = input()
        teachings.append(tch)
        yy = input  ('Got some more? [y/n]').lower().startswith('y')
        if yy is not True:
            break
    nLeaves = 12
    cur = program.getConn().cursor()
    cur.execute("insert into faculty(ID, noOfLeaves, department) values (%s, %s, %s);  ", (str(email), int(nLeaves), str(Department)))
    state.active_account = svc.create_account(name, email, Department, publications, grants, awards, teachings)
    program.getConn().commit()
    success_msg(f"Created new account with id {state.active_account.id}.")


def edit_your_profile():
    print(' ****************** EDIT YOUR PROFILE **************** ')
    
    email = input('What is your email? ').strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    print('************ IN GUI ************')
    

def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email? ').strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account
    print(state.active_account.id)
    success_msg('Logged in successfully.')


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('[L]ogin to your account')
    print('[E]dit profile')
    print('View [y]our Profile')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def view_your_profile():
    print(' ****************** Your Profile **************** ')
    if not state.active_account:
        error_msg("You must log in first to view your snakes")
        return

    info = svc.getInfo(state.active_account.id)
    for i in info:
        print('')
        for j in i:
            print(j)


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
