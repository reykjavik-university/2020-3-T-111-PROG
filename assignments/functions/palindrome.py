def palindrome(s):
    '''Returns True if the given string is a palindrome and False otherwise.'''
    s_clean = ''
    for ch in s:
        if ch.isalnum():
            s_clean += ch.lower()
    return s_clean == s_clean[::-1]

in_str = input("Enter a string: ")
print('"{:s}" is '.format(in_str),end='')
if not palindrome(in_str):
    print("not ", end = '')
print("a palindrome.")