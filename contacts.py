print("CONTACT BOOK")
print("STORE AND AMNAGE YOUR CONTACTSA HERE")
print("Enter 'ADD' to add Contacts")
print("Enter 'INFO' to delete Contact Information")
print("Enter 'UPDATE' to update Contacts") 
print("Enter 'DELETE' to delete Contact")
print("Enter 'SEARCH' to search Contact")
print("Enter 'VIEW' to view Contacts")
print("Enter 'EXIT' to exit")
Contacts=[]
while True:
    option=input('Enter your option": ').upper()
    if option == 'ADD':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contact = {
            "name" : name,
            "phone" : phone,
            "email" : email,
            "address" : address
            }

        Contacts.append(contact)
        print('Contact added!')
    elif option =='UPDATE':
        if not Contacts:
            print("No contacts to be updated")
        else:
            print("Current contacts: ")
            for i in range(len(Contacts)):
                c = Contacts[i]
                print(f"Contact - {i} Name : {c['name']}, Phone :  {c['phone']}, Email : {c['email']}, Address : {c['address']} ")
            try:
               index=int(input(" Enter the Contact number to be updated (Contact number starts from 0): "))
               if 0<=index<len(Contacts):
                    name = input("Enter name: ")
                    phone = input("Enter phone number: ")
                    email = input("Enter email address: ")
                    address = input("Enter address: ")
                    Contacts[index] = {
                    "name" : name,
                    "phone" : phone,
                    "email" : email,
                    "address" : address
                    }
                    print("Contact updated successfully")
               else:
                    print("Invalid Contact number") 
            except ValueError:
                print("Enter a valid number: ")

    elif option == 'DELETE':
        if not Contacts:
            print("No contact to be deleted")
        else:
             print("Current Contacts: ")
             for i in range(len(Contacts)):
                 c = Contacts[i]
                 print(f"Contact - {i} Name : {c['name']}, Phone :  {c['phone']}, Email : {c['email']}, Address : {c['address']} ")
             try:
                index=int(input(" Enter the Contact number to be deleted (Contact number starts from 0): "))
                if 0<=index<len(Contacts):
                    deleted_contact=Contacts.pop(index)
                    print(f"Deleted contact :  {deleted_contact['name']}")
                else:
                    print("Invalid contact number")
             except ValueError:
                print("Enter a valid number: ")

    elif option == 'SEARCH':
        if not Contacts:
            print("No contacts to search")
        else:
            keyword = input("Enter name or phone number to search: ").lower()
            found=False
            for c in Contacts:
                if keyword in c['name'].lower() or keyword in c['phone']:
                    print(f"Name : {c['name']}, Phone :  {c['phone']}, Email : {c['email']}, Address : {c['address']} ")
                    found = True
                if not found:
                    print("No matching contact found")

    elif option == 'VIEW':
         if not Contacts:
            print("No contacts found!!")
         else:
             for i in range(len(Contacts)):
                 c = Contacts[i]
                 print(f"Contact - {i} Name : {c['name']}, Phone :  {c['phone']}, Email : {c['email']}, Address : {c['address']} ")


    elif option =='EXIT':
        print ("Exited....")
        break
    


