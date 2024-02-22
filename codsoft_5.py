from os import system
from re import search, IGNORECASE
from sys import exit
from time import sleep


class Contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Number: {contact.number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("-" * 20)
        else:
            system("clear")
            print("-" * 20)
            print("No Contacts To View")
            print("-" * 20)

    def search_contact(self, search):
        for contact in self.contacts:
            if search in contact.name or search in contact.number:
                print("-" * 20)
                print(f"Name: {contact.name}")
                print(f"Number: {contact.number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("-" * 20)
                return

        system("clear")
        print("-" * 20)
        print(f"Contact {search} Not Found")
        print("-" * 20)
        sleep(1)

    def update_contact(self, name, new_details):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = new_details.get("name", contact.name)
                contact.number = new_details.get("number", contact.number)
                contact.email = new_details.get("email", contact.email)
                contact.address = new_details.get("address", contact.address)
                return

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("-" * 20)
                print(f"Contact '{name}' Deleted Successfully")
                print("-" * 20)
            else:
                system("clear")
                print("-" * 20)
                print(f"Contact '{name}' Not Found")
                print("-" * 20)


contact_book = ContactBook()


def main():
    while True:
        system("clear")
        print("-" * 20)
        print("        MENU")
        print("-" * 20)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            system("clear")
            exit("Bye Bye")

        else:
            system("clear")
            print("-" * 20)
            print("Invalid Choice")
            print("-" * 20)
            sleep(1)


def add_contact():
    system("clear")
    print("-" * 20)
    print("    ADD CONTACT")
    print("-" * 20)

    name = input("Enter Name: ").strip().title()

    while True:
        number = input("Enter Number: ")
        if search(r"^03\d{2}-\d{7}", number) and len(number) == 12:
            break
        print("-" * 20)
        print("Invalid Phone Number Use [03XX-XXXXXXX] Format")
        print("-" * 20)

    while True:
        email = input("Enter Email: ").strip()
        if search(r"^\w+@\w+\.[a-zA-Z]{2,}$", email, IGNORECASE):
            break
        print("-" * 20)
        print("Invalid Email")
        print("-" * 20)

    address = input("Enter Address: ")

    contact = Contact(name, number, email, address)
    contact_book.add_contact(contact)

    system("clear")
    print("-" * 20)
    print("Contact Added Successfully!")
    print("-" * 20)
    sleep(1)


def view_contact():
    system("clear")
    print("-" * 20)
    print("   VIEW CONTACTS")
    print("-" * 20)

    contact_book.view_contact()

    choice = input("To Exit [x]: ")
    if choice.lower() == "x":
        return


def search_contact():
    system("clear")
    print("-" * 20)
    print("   SEARCH CONTACT")
    print("-" * 20)

    contact_book.search_contact(input("Search: ").strip().title())

    choice = input("To Exit [x]: ")
    if choice.lower() == "x":
        return


def update_contact():
    system("clear")

    for contact in contact_book.contacts:
        name = input("Contact To Update: ").strip().title()
        if contact.name == name:
            while True:
                system("clear")
                print("-" * 20)
                print("  UPDATE CONTACTS")
                print("-" * 20)
                print("Current Details:")
                contact_book.search_contact(name)
                print("\nUPDATE: ")
                print("1. Phone Number")
                print("2. Email")
                print("3. Address")

                update_choice = input("Enter your choice: ")

                updates = {}
                if update_choice == "1":
                    while True:
                        new_number = input("New Number: ")
                        if new_number == "":
                            break
                        elif (
                            search(r"^03\d{2}-\d{7}", new_number)
                            and len(new_number) == 12
                        ):
                            updates["number"] = new_number
                            break

                        print("-" * 20)
                        print("Invalid Phone Number Use [03XX-XXXXXXX] Format")
                        print("-" * 20)

                elif update_choice == "2":
                    while True:
                        new_email = input("Enter Email: ").strip()
                        if new_email == "":
                            break
                        elif search(r"^\w+@\w+\.[a-zA-Z]{2,}$", new_email, IGNORECASE):
                            updates["email"] = new_email
                            break

                        print("-" * 20)
                        print("Invalid Email")
                        print("-" * 20)

                elif update_choice == "3":
                    new_address = input("New Address: ")
                    if new_address:
                        updates["address"] = new_address

                else:
                    print("Invalid Choice")

                if updates:
                    confirmation = input("Confirm Update? [y/n]: ")
                    if confirmation.lower() == "y":
                        contact_book.update_contact(name, updates)
                        print("-" * 20)
                        print(f"Contact '{name}' Updated Successfully!")
                        print("-" * 20)
                        sleep(1)
                    else:
                        system("clear")
                        print("-" * 20)
                        print("Update Cancelled")
                        print("-" * 20)
                        sleep(1)

                choice = input("Want To Exit [y/n]: ")
                if choice.lower() == "y":
                    break
            return
        else:
            system("clear")
            print("-" * 20)
            print(f"Contact '{name}' Not Found.")
            print("-" * 20)
            sleep(1)
            return

    system("clear")
    print("-" * 20)
    print(f"No Contacts Found.")
    print("-" * 20)
    sleep(1)
    return


def delete_contact():
    system("clear")
    print("DELETE CONTACT")
    print("-" * 20)

    contact_book.delete_contact(input("Name: ").strip().title())
    sleep(1)


if __name__ == "__main__":
    main()
