''' 
Name: Jhalak choudhary
Date: 12-Nov-2025
Assignment Title: Contact Manager - Assignment 02
Project: Contact Book Management System
'''

import csv
import json
from datetime import datetime

print("\nWelcome to the Contact Book!")
print("This tool helps you record and manage contacts efficiently.\n")

CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json"
LOG_FILE = "error_log.txt"


def log_error(message, operation):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] Operation: {operation} | Error: {message}\n")


def add_contact():
    try:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {"name": name, "phone": phone, "email": email}

        file_exists = False
        try:
            with open(CSV_FILE, "r"):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(contact)

        print("\nContact added successfully!\n")

    except Exception as e:
        print("Error adding contact.")
        log_error(str(e), "Add Contact")


def display_contacts():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

            if not contacts:
                print("No contacts found.")
                return

            print("\n----- CONTACT LIST -----")
            print("Name\t\tPhone\t\tEmail")
            print("-" * 50)

            for c in contacts:
                print(f"{c['name']}\t\t{c['phone']}\t\t{c['email']}")
            print()

    except FileNotFoundError:
        print("Contacts file not found.")
        log_error("CSV file missing", "Display Contacts")

    except Exception as e:
        print("Error reading contacts.")
        log_error(str(e), "Display Contacts")


def search_contact():
    name = input("Enter the name to search: ")

    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)

            for c in reader:
                if c["name"].lower() == name.lower():
                    print("\nContact Found:")
                    print(f"Name: {c['name']}")
                    print(f"Phone: {c['phone']}")
                    print(f"Email: {c['email']}\n")
                    return

        print("Contact not found.\n")

    except Exception as e:
        print("Error searching contact.")
        log_error(str(e), "Search Contact")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    try:
        with open(CSV_FILE, "r") as file:
            contacts = list(csv.DictReader(file))

        found = False
        for c in contacts:
            if c["name"].lower() == name.lower():
                found = True
                print("\nWhat do you want to update?")
                print("1. Phone")
                print("2. Email")

                choice = input("Enter choice: ")
                if choice == "1":
                    c["phone"] = input("Enter new phone: ")
                elif choice == "2":
                    c["email"] = input("Enter new email: ")
                else:
                    print("Invalid choice.")
                    return

        if not found:
            print("Contact not found.")
            return

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows(contacts)

        print("\nContact updated successfully!\n")

    except Exception as e:
        print("Error updating contact.")
        log_error(str(e), "Update Contact")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    try:
        with open(CSV_FILE, "r") as file:
            contacts = list(csv.DictReader(file))

        new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]

        if len(new_contacts) == len(contacts):
            print("Contact not found.")
            return

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows(new_contacts)

        print("\nContact deleted successfully!\n")

    except Exception as e:
        print("Error deleting contact.")
        log_error(str(e), "Delete Contact")


def export_to_json():
    try:
        with open(CSV_FILE, "r") as file:
            contacts = list(csv.DictReader(file))

        with open(JSON_FILE, "w") as jf:
            json.dump(contacts, jf, indent=4)

        print("\nContacts exported to JSON successfully!\n")

    except Exception as e:
        print("Error exporting to JSON.")
        log_error(str(e), "Export JSON")


def load_from_json():
    try:
        with open(JSON_FILE, "r") as jf:
            contacts = json.load(jf)

        print("\n----- CONTACTS FROM JSON -----")
        print("Name\t\tPhone\t\tEmail")
        print("-" * 50)
        for c in contacts:
            print(f"{c['name']}\t\t{c['phone']}\t\t{c['email']}")
        print()

    except Exception as e:
        print("Error loading JSON.")
        log_error(str(e), "Load JSON")


def main():
    print("\nWelcome to the Contact Book Management System")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Load from JSON")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            export_to_json()
        elif choice == "7":
            load_from_json()
        elif choice == "8":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
