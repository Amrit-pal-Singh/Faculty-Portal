from colorama import Fore
import psycopg2
import program_profs
import data.mongo_setup as mongo_setup

try:
    conn = psycopg2.connect(database = "project", user = "postgres", password = "123456789", host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
except:
    print("Error Opening Database")


def getConn():
    return conn

def main():
    mongo_setup.global_init()
    print_header()
    program_profs.run()


def print_header():
    welcome = \
        """
        Welcome To IIT ROPAR Faulty portal
        """

    print(Fore.WHITE + '*********************************************')
    print(Fore.GREEN + welcome)
    print(Fore.WHITE + '*********************************************')
    print()

if __name__ == '__main__':
    main()
