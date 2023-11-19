class Assistant:
    def __init__(self):
        self.contacts = {}

    def input_error(func):
        def wrapper(self, *args):
            try:
                return func(self, *args)
            except KeyError:
                return "Enter user name"
            except ValueError:
                return "Give me name and phone please"
            except IndexError:
                return "Invalid command format"

        return wrapper

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change_phone(self, name, phone):
        if name not in self.contacts:
            raise KeyError
        self.contacts[name] = phone
        return f"Phone number for {name} updated to {phone}"

    @input_error
    def show_phone(self, name):
        return f"The phone number for {name} is {self.contacts[name]}"

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found."
        result = "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())
        return result

    def exit(self):
        return "Good bye!"

    def main(self):
        while True:
            try:
                command = input("Enter a command: ").lower()
                if command in ("good bye", "close", "exit", "."):
                    print(self.exit())
                    break
                elif command == "hello":
                    print("How can I help you?")
                elif command.startswith("add"):
                    _, *data = command.split(" ", 2)
                    if len(data) == 2:
                        name, phone = data
                        print(self.add_contact(name, phone))
                    else:
                        print("Invalid command format. Please provide both name and phone.")
                elif command.startswith("change"):
                    _, *data = command.split(" ", 2)
                    if len(data) == 2:
                        name, phone = data
                        print(self.change_phone(name, phone))
                    else:
                        print("Invalid command format. Please provide both name and phone.")
                elif command.startswith("phone"):
                    _, name = command.split(" ", 1)
                    print(self.show_phone(name))
                elif command == "show all":
                    print(self.show_all_contacts())
                else:
                    print("Invalid command. Try again.")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    assistant = Assistant()
    assistant.main()
