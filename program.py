from colorama import Fore
import program_profs
import data.mongo_setup as mongo_setup

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
