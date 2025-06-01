# learn module makes it easier to separate code into multiple files
# and reuse them,
# import module
# module.function()

def say_gello(name): 
    return f'Hello, {name}'

def total(*args):
    result = 0
    for i in args:
        result += i
    return result


## view contact
def display_contact(contact_list):
    for contact in contact_list:
        print("======================")
        print(f"name :{contact['name']}")
        print(f"phone : {contact['phone']}")
        print(f"email: {contact['email']}")

def add_contact():
    name = input("Name : ")
    phone = input("Phone : ")
    email = input("Email : ")

    contact = {
        'name' : name,
        'phone' : phone,
        'email' : email
    }

    return contact

# find contact
def find_contact(contact_list):
    name = input("Name : ")
    for contact in contact_list:
        # nama_contact = contact['name'].lower()
        # if nama_contact.find(name.lower()) != -1:
        if name in contact['name'].lower():
            print("======================")
            print(f"name :{contact['name']}")
            print(f"phone : {contact['phone']}")
            print(f"email: {contact['email']}")

            return contact
    print("Contact not found")
    return None

def remove_contact(contact_list):
    phone_number = input("Phone Number: ")
    for contact in contact_list:
        if contact['phone'] == phone_number:
            contact_list.remove(contact)
            print(f"Contact removed {phone_number}")
            return True
    print("Contact not found")
    return None
