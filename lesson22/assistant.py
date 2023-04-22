from handlers import *

COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact, 'show_phone': show_phone,
            'show all': show_all, 'exit': goodbye, 'close': goodbye, '.': goodbye, 'stop': goodbye, 'help': help_me}

# add Sasha +380937316048
def main():
    contacts = {}
    while True:
        user_command = input('Enter command: ')
        for key in COMMANDS.keys():
            if user_command.lower().startswith(key):
                args = user_command[len(key):].split()
                result = COMMANDS.get(key, None)(contacts, *args)
                if result is None:
                    print('Good Bye!')
                    exit(0)
                print(result, '\n')
                break
        else:
            print('Unknown command! Enter again!\n')


if __name__ == "__main__":
    main()













if __name__ == "__main__":
    main()