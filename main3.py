# Modul 5 Home work 4

def input_error(func): #Обгортає функції-обробники команд і перехоплює помилки.
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error #Додає новий контакт у словник contacts.
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error #Змінює номер телефону існуючого контакту.
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error #Показує номер телефону для зазначеного контакту.
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


@input_error #Виводить усі контакти з номерами.
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def parse_input(user_input): #Розбиває введений рядок на команду (cmd) і аргументи (args).
    parts = user_input.split()
    if not parts:  # Якщо пустий рядок
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


def main(): #Створюємо словник.
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            print("You entered nothing. Try again.")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
#Перевірка.
#Вводимо команди.