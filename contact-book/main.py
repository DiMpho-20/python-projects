from contacts import add_contact, search_contact, delete_contact

def main():
    while True:
        print('\n--- Contact Book ---')
        print('1. Add contact')
        print('2. Search contact')
        print('3. Delete contact')
        print('4. Exit')

        
        choice = input('Choose an option: ')
        
        if choice == '1':
            name = input('Name: ')
            phone = input('Phone: ')
            email = input('Email: ')
            add_contact(name, phone, email)
        elif choice == '2':
            name = input('Search name: ')
            search_contact(name)
        elif choice == '3':
            name = input('Enter name to delete: ')
            delete_contact(name)
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid option, try again.')
if __name__ == "__main__":
    main()