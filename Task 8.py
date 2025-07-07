def add_contact(contact_book, name, phone, email):

    if name in contact_book:
        print(f"Contact '{name}' already exists.")
    else:
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.")


def update_contact(contact_book, name, phone=None, email=None):

    if name not in contact_book:
        print(f"Contact '{name}' does not exist.")
        return

    if phone:
        contact_book[name]["phone"] = phone
    if email:
        contact_book[name]["email"] = email

    print(f"Contact '{name}' updated successfully.")


def retrieve_contact(contact_book, name):

    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"Contact '{name}' not found.")


def view_all_contacts(contact_book):

    if not contact_book:
        print("Contact book is empty.")
        return

    print("All Contacts:")
    print("-" * 40)
    for name, info in contact_book.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print("-" * 40)


def contact_book_manager():

    contact_book = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            add_contact(contact_book, name, phone, email)

        elif choice == '2':
            name = input("Enter the name of the contact to update: ").strip()
            print("Leave field blank if no change.")
            phone = input("Enter new phone: ").strip()
            email = input("Enter new email: ").strip()

            phone = phone if phone else None
            email = email if email else None

            update_contact(contact_book, name, phone, email)

        elif choice == '3':
            name = input("Enter the name of the contact to retrieve: ").strip()
            retrieve_contact(contact_book, name)

        elif choice == '4':
            view_all_contacts(contact_book)

        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    contact_book_manager()
