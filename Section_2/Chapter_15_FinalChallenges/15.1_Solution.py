def validation_email_format(email):
    #filter outt bad emails
    if(email[0] == "@" or email[len(email)-1] == "@"):
        return False
    elif(email[0] == "." or email[len(email)-1] == "."):
        return False
    elif(email.count('@') != 1 and email.count('.') != 1):
        return False
    elif(email.count(' ') > 0):
        return False
    return True

def validate_phonenumber(phonenumber):
    if(len(phonenumber) != 10):
        return False
    return True

def clean_numbers(phonenumber):
    new_number = ""
    for i in phonenumber:
        if(i.isdigit()):
            new_number += i
    return new_number

def remove_duplicates(contacts):
    found = True
    while(found):
        found = False
        for i in range(0,len(contacts)):
            for j in range(0,len(contacts)):
                if(i != j):
                    if contacts[i]["email"] == contacts[j]["email"]:
                        found = True
                        contacts.pop(j)
                        break
                    if contacts[i]["phone"] == contacts[j]["phone"]:
                        found = True
                        contacts.pop(j)
                        break 
            if(found == True):
                break
    return contacts
def organize_contacts(contact_list):
    # Your solution here
    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    for contact in contact_list:
        contact["phone"] = clean_numbers(contact["phone"])
        contact["email"] = contact["email"].lower()
    temp_contacts = filter(lambda x : validation_email_format(x["email"]), contact_list)
    new_contacts = filter(lambda x : validate_phonenumber(x["phone"]), temp_contacts) 
    new_contacts = remove_duplicates(list(new_contacts))       
    # 3. Return the clean contact list
    return list(new_contacts)

    pass
