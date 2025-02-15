import json
import os

# ANSI escape codes for colors
class Colors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

# File to store contacts
CONTACTS_FILE = 'contacts.json'

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

def add_contact(contacts):
    """Add a new contact."""
    name = input(Colors.CYAN + "Enter contact name: " + Colors.RESET)
    phone = input(Colors.CYAN + "Enter contact phone number: " + Colors.RESET)
    
    if name in contacts:
        print(Colors.RED + f"Contact {name} already exists." + Colors.RESET)
    else:
        contacts[name] = {'phone': phone}
        save_contacts(contacts)
        print(Colors.GREEN + f"Contact {name} added successfully." + Colors.RESET)

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print(Colors.YELLOW + "No contacts found." + Colors.RESET)
    else:
        print(Colors.GREEN + "Contacts:" + Colors.RESET)
        for name, info in contacts.items():
            print(Colors.BLUE + f"{name}: Phone: {info['phone']}" + Colors.RESET)

def search_contact(contacts):
    """Search for a contact by name."""
    name = input(Colors.CYAN + "Enter the name of the contact to search: " + Colors.RESET)
    if name in contacts:
        info = contacts[name]
        print(Colors.GREEN + f"{name}: Phone: {info['phone']}" + Colors.RESET)
    else:
        print(Colors.RED + f"Contact {name} not found." + Colors.RESET)

def update_contact(contacts):
    """Update an existing contact."""
    name = input(Colors.CYAN + "Enter the name of the contact to update: " + Colors.RESET)
    if name in contacts:
        phone = input(Colors.CYAN + "Enter new phone number: " + Colors.RESET)
        contacts[name] = {'phone': phone}
        save_contacts(contacts)
        print(Colors.GREEN + f"Contact {name} updated successfully." + Colors.RESET)
    else:
        print(Colors.RED + f"Contact {name} not found." + Colors.RESET)

def delete_contact(contacts):
    """Delete a contact."""
    name = input(Colors.CYAN + "Enter the name of the contact to delete: " + Colors.RESET)
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(Colors.GREEN + f"Contact {name} deleted successfully." + Colors.RESET)
    else:
        print(Colors.RED + f"Contact {name} not found." + Colors.RESET)

def main():
    contacts = load_contacts()
    
    while True:
        print(Colors.MAGENTA + "\nContact Book" + Colors.RESET)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input(Colors.CYAN + "Choose an option: " + Colors.RESET)
        
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
            print(Colors.GREEN + "Exiting the contact book. Goodbye!" + Colors.RESET)
            break
        else:
            print(Colors.RED + "Invalid choice. Please try again." + Colors.RESET)

if __name__ == "__main__":
    main()
