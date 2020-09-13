email_address = input("Email address: ")
print("Checking...")

local_part, at_symbol, domain = email_address.partition("@")
if at_symbol != "@":
    print("@ symbol is missing")
elif len(local_part) == 0:
    print(" {}".format(email_address))
    print("^--this bit is missing")
elif local_part.startswith("."):
    print(email_address)
    print("^--there's a dot here that probably shouldn't")
elif local_part.endswith("."):
    padding = " " * (len(local_part) - 1)
    print(email_address)
    print(padding + "^--there's a dot here that probably shouldn't")
elif ".." in email_address:
    start_index = email_address.find("..")
    padding = " " * start_index
    print(email_address)
    print(padding + "^--there are consecutive dots here")
elif len(domain) == 0:
    padding = " " * len(email_address)
    print(email_address)
    print(padding + "^--this bit is missing")
elif "@" in domain:
    index = email_address.find("@", len(local_part) + 1)
    padding = " " * index
    print(email_address)
    print(padding + "^--there's an extra @ symbol here")
elif "." not in domain:
    print(f"The top-level-domain is missing. Did you perhaps intend to write {email_address}.com?")
else:
    print("Seems legit")
