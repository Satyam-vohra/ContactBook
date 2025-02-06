import json
import os
import re
import getpass

# File to store contacts
CONTACTS_FILE = 'contacts.json'
BACKUP_FILE = 'contacts_backup.json'

# User authentications
USER_CREDENTIALS = {'satyam vohra': 'satyam'}  # Example credentials

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def backup_contacts():
    """Backup contacts to a backup file."""
    with open(BACKUP_FILE, 'w') as file:
        json.dump(load_contacts(), file, indent=4)
    print("Contacts backed up successfully.")

def is_valid_phone(phone):
    """Check if the phone number is valid (digits only and 10 digits long)."""
    return re.match(r'^\d{10}$', phone) is not None

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ")
    
    # Validate phone number
    phone = input("Enter contact phone number: ")
    while not is_valid_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone = input("Enter contact phone number: ")
    
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        contacts[name] = {'phone': phone}
        save_contacts(contacts)
        print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f" {name}: Phone: {info['phone']}")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"{name}: Phone: {info['phone']}")
    else:
        print(f"Contact {name} not found.")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        while not is_valid_phone(phone):
            print("Invalid phone number. Please enter a 10-digit number.")
            phone = input("Enter new phone number: ")
        
        contacts[name] = {'phone': phone}
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def authenticate_user():
    """Authenticate user."""
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False

def main():
    if not authenticate_user():
        return  # Exit if authentication fails

    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Backup Contacts")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            backup_contacts()
        elif choice == '7':
            print("Exiting the contact book. Goodbye!")
            break    
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
