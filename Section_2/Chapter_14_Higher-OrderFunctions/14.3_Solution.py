def clean_email_list(emails):
    # Write your code below   
    valid_emails = filter(
        lambda x : x[0] != '@' and x[len(x)-1] != '@', filter(
            lambda x : x.count('@') == 1, map(
                lambda x : x.replace(" ", "").lower(), emails)))
    return list(valid_emails)
