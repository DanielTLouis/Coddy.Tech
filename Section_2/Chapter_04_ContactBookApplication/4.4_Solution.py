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
  else:
    print("Contact not found!")
