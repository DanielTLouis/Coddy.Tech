def is_empty(dictionary):
   for i in dictionary:
      if i : 
         return False; 
   return True; 
def list_all_contacts(contact_book):
   if(is_empty(contact_book)):
      print("No contacts available.")
   else:
      for contact in contact_book.keys():
         print("Name: " + contact)
         print("Phone: " + contact_book[contact]["phone"])
         print("Email: " + contact_book[contact]["email"])
         print("Address: " + contact_book[contact]["address"])
         print()
         
def delete_contact(contact_book):
   name = input() 
   if(contact_book.get(name)):
      del contact_book[name]
      print("Contact deleted successfully!")
   else:
      print("Contact not found!")

def edit_contact(contact_book):
   name = input() 
   if(contact_book.get(name)):
      phone = input()
      email = input()
      address = input() 
      if(phone != ""):
         contact_book[name]["phone"] = phone 
      if(email != ""):
         contact_book[name]["email"] = email 
      if(address != ""):
         contact_book[name]["address"] = address
      print("Contact updated successfully!")
      return contact_book 
   else:
      print("Contact not found!")
def add_contact(contact_book):
   name = input()
   phone = input()
   email = input()
   address = input()
   if(contact_book.get(name)):
      print("Contact already exists!")
   else:
      contact_book[name] = {"phone": phone, "email": email, "address": address}
      print("Contact added successfully!")
def view_contact(contact_book):
   name = input()
   if(contact_book.get(name)):
      print("Name: " + name)
      print("Phone: " + contact_book[name]["phone"])
      print("Email: " + contact_book[name]["email"])
      print("Address: " + contact_book[name]["address"])
   else: 
      print("Contact not found!")
def display_menu():
   print("Contact Book Menu:")
   print("1. Add Contact")
   print("2. View Contact")
   print("3. Edit Contact")
   print("4. Delete Contact")
   print("5. List All Contacts")
   print("6. Exit")

contact_book = {}
while True:
   display_menu()
   user_input = int(input())
   match user_input:
      case 1:
         add_contact(contact_book)
      case 2:
         view_contact(contact_book)
      case 3:
         edit_contact(contact_book)
      case 4:
         delete_contact(contact_book)
      case 5:
         list_all_contacts(contact_book)
      case 6:
         break 
      case _: 
         print("Please select from menu")
      
