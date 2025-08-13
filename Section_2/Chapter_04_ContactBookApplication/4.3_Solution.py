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
def view_content(content_book):
  name = input()
  if(content_book.get(name)):
    print("Name: " + name)
    print("Phone: " + contact_book[name]["phone"])
    print("Email: " + contact_book[name]["email"])
    print("Address: " + contact_book[name]["address"])
  else:
    print("Contact not found!")
