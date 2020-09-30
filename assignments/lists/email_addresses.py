def get_names_and_domains(list_of_emails):
    result_list = []
    for address in list_of_emails:
        uname, domain = address.split('@')
        result_list.append((uname,domain))

    return result_list

def get_emails():
    email_list = []
    email = input('Email address: ')
    while email != 'q':
        email_list.append(email)
        email = input('Email address: ')

    return email_list

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)   
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)