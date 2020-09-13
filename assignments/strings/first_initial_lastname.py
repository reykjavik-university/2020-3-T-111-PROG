name = input("Input a name: ")
name = name.capitalize()
index_space = name.find(" ")

firstname = name[index_space+1:]
lastname = name[:index_space-1]
display_name = firstname[0].upper() + ". " + lastname
print(display_name)