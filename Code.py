# Predefined emergency contacts
emergency_contacts = {
    "Fire Department": "101",
    "Police": "100",
    "Ambulance": "102",
    "Disaster Helpline": "108",
}

def get_emergency_contact(service):
    """Retrieve emergency contact by service name."""
    return emergency_contacts.get(service, "Service not found. Try adding it.")

def add_emergency_contact(service, number):
    """Add a new emergency contact."""
    emergency_contacts[service] = number
    print(f"✅ {service} contact saved successfully!")

def list_emergency_contacts():
    """Display all stored emergency contacts."""
    print("\n📞 Emergency Contacts List:")
    for service, number in emergency_contacts.items():
        print(f"{service}: {number}")

# User menu
while True:
    print("\n🚨 Emergency Contact System 🚨")
    print("1. Get Contact")
    print("2. Add New Contact")
    print("3. List All Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        service_name = input("Enter the emergency service name: ")
        print("Contact:", get_emergency_contact(service_name))
    elif choice == "2":
        service_name = input("Enter new service name: ")
        contact_number = input("Enter contact number: ")
        add_emergency_contact(service_name, contact_number)
    elif choice == "3":
        list_emergency_contacts()
    elif choice == "4":
        print("Exiting... Stay Safe! 🚑🚒🚓")
        break
    else:
        print("Invalid choice! Please enter a number between 1-4.")
