def add_contact(contact_book):
  name = input()
  phone = input()
  email = input()
  address = input()
  if(contact_book.get(name)):
    print("Contact already e><ists!")
  else:
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")
