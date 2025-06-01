import function

## contact management

# list of dictianory 
contact_list = []
contact_list.append({'name': 'John', 'phone': '1234567890', 'email': 'john@example.com'})
contact_list.append({'name': 'Jane', 'phone': '0987654321', 'email': 'john@example.com'})

# program menu
while True: 
    print('1. Add contact')
    print('2. View contact')
    print('3. Search contact')
    print('4. Delete contact')
    print('0. Exit')

    menu = input('Enter your choice: ')

    if(menu == "0"):
        break
    elif(menu == "1"):
        # add contact
        new_contact = function.add_contact()
        contact_list.append(new_contact)
    elif(menu == "2"):
        # view contact
        function.display_contact(contact_list)
    elif(menu == "3"):
        # search contact
        function.find_contact(contact_list)
    elif(menu == "4"):
        # delete contact
        function.remove_contact(contact_list)
    else:
        print('Invalid choice')
    

print(contact_list)
print("program ended")