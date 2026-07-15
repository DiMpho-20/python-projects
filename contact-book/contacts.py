import json
from config import FILENAME


def load_contacts():
    try:
        with open(FILENAME) as f:
            return json.load(f) # convert into a python list
    
    except FileNotFoundError:
        return []
    
def save_contact(contacts):
    with open(FILENAME,'w' ) as f:
        json.dump(contacts,f,indent=2)
    
def add_contact(name,phone,email):
    contacts = load_contacts()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email})
    
    save_contact(contacts)
    print(f'Contact {name} added.')

def search_contact(name):
    contacts=load_contacts()
    results=[c for c in contacts if name.lower() in c['name'].lower()]

    if not results:
        print(f'No contacts found for "{name}"')
        return

    for c in results:
        print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

def delete_contact(name):
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name.lower()]

    if len(updated) == len(contacts):
        print(f'No contact found with name "{name}"')
        return
    
    save_contact(updated)
    print(f'Contact "{name}" deleted.')

