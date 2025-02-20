import json

CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
        return contacts
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContacts List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}\n")

# Add a new contact
def add_contact(contacts):
    name = input("\nEnter the contact's name: ")
    if name in contacts:
        print(f"A contact with the name '{name}' already exists.")
    else:
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact for {name} added successfully!")

# Update an existing contact
def update_contact(contacts):
    name = input("\nEnter the contact's name you want to update: ")
    if name in contacts:
        print(f"Updating contact for {name}.")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"No contact found for {name}.")

# Delete a contact
def delete_contact(contacts):
    name = input("\nEnter the contact's name you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found for {name}.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            
# import emoji module
import emoji

# smiling face
  print("\N{smiling face")
  print(emoji.emojize(":smiling face:"))
  print("\nGoodbye and Thankyou!")
  break
else:
    print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()
    

