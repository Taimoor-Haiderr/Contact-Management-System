import json
import os
import re

FILE_NAME = "contacts.json"

# ---------------- LOAD DATA ----------------
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# ---------------- SAVE DATA ----------------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# ---------------- GENERATE ID ----------------
def generate_id(contacts):
    return max([c["id"] for c in contacts], default=0) + 1

# ---------------- VALIDATION ----------------
def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

# ---------------- ADD CONTACT ----------------
def add_contact(contacts):
    print("\n--- Add Contact ---")

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    city = input("City: ").strip()
    company = input("Company: ").strip()

    if not all([name, phone, email, city, company]):
        print("❌ All fields required!")
        return

    if not valid_email(email):
        print("❌ Invalid email!")
        return

    if not valid_phone(phone):
        print("❌ Invalid phone!")
        return

    contact = {
        "id": generate_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "company": company
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added!")

# ---------------- VIEW CONTACTS ----------------
def view_contacts(contacts):
    print("\n--- Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    print(f"{'ID':<5}{'Name':<20}{'Phone':<15}{'Email':<25}{'City':<15}{'Company'}")
    print("-"*90)

    for c in contacts:
        print(f"{c['id']:<5}{c['name']:<20}{c['phone']:<15}{c['email']:<25}{c['city']:<15}{c['company']}")

# ---------------- SEARCH ----------------
def search_contacts(contacts):
    keyword = input("\nSearch: ").lower()

    results = [c for c in contacts if
               keyword in c["name"].lower() or
               keyword in c["phone"] or
               keyword in c["email"].lower()]

    if not results:
        print("❌ No match found.")
        return

    for c in results:
        print(c)

# ---------------- FILTER ----------------
def filter_contacts(contacts):
    print("\n1. By City\n2. By Company")
    choice = input("Choose: ")

    keyword = input("Enter value: ").lower()

    if choice == "1":
        results = [c for c in contacts if keyword in c["city"].lower()]
    elif choice == "2":
        results = [c for c in contacts if keyword in c["company"].lower()]
    else:
        print("Invalid choice")
        return

    for c in results:
        print(c)

# ---------------- UPDATE ----------------
def update_contact(contacts):
    try:
        cid = int(input("Enter ID: "))
    except:
        print("Invalid ID")
        return

    for c in contacts:
        if c["id"] == cid:
            print("Leave blank to skip")

            c["name"] = input("New Name: ") or c["name"]
            c["phone"] = input("New Phone: ") or c["phone"]
            c["email"] = input("New Email: ") or c["email"]
            c["city"] = input("New City: ") or c["city"]
            c["company"] = input("New Company: ") or c["company"]

            save_contacts(contacts)
            print("✅ Updated!")
            return

    print("❌ Not found")

# ---------------- DELETE ----------------
def delete_contact(contacts):
    try:
        cid = int(input("Enter ID: "))
    except:
        print("Invalid ID")
        return

    for c in contacts:
        if c["id"] == cid:
            contacts.remove(c)
            save_contacts(contacts)
            print("✅ Deleted!")
            return

    print("❌ Not found")

# ---------------- MAIN MENU ----------------
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGER =====")
        print("1. Add Contacts")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Filter Contacts")
        print("5. Update Contacts")
        print("6. Delete Contact")
        print("7. Exit")

        choice = input("Enter: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            filter_contacts(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

