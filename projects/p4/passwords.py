MIN_LENGTH = 6
MAX_LENGTH = 20

total_count = 0
total_valid = 0
total_invalid = 0

passwd = input("Enter a new password: ")

while passwd != 'q':
    total_count += 1
    length = len(passwd)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        print("Invalid length")
        total_invalid += 1
    
    else:
        found_lower = False
        found_upper = False
        found_number = False
        for i in range(0, length):
            ch = passwd[i]
            if ch.islower():
                found_lower = True
            if ch.isupper():
                found_upper = True
            if ch.isnumeric():
                found_number = True

        if not found_lower:
            print("At least one lower case letter needed")
        if not found_upper:
            print("At least one upper case letter needed")
        if not found_number:
            print("At least one number needed")
        
        if found_lower and found_upper and found_number:
            total_valid += 1
            print("Valid password of length", length)
        else:
            total_invalid += 1

    passwd = input("Enter a new password: ")

print("You tried {} passwords, {} valid, {} invalid".format(total_count, total_valid, total_invalid))