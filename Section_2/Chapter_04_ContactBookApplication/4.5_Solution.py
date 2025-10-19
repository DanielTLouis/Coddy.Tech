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
         contact_book[name][phone] = phone 
      if(email != ""):
         contact_book[name][email] = email 
      if(address != ""):
         contact_book[name][address] = address
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
