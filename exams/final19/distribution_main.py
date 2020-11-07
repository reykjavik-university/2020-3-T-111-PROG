from distribution import Distribution

def open_file(filename):
        ''' Returns a file stream if filename found, otherwise None '''
        try:
            file_stream = open(filename, "r")
            return file_stream
        except FileNotFoundError:
            return None

# Main starts here
dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4})
print("Dist1: ")
print(dist1)
print(dist1.average())

filename = input("Enter filename: ")
file_stream = open_file(filename)

dist2 = Distribution(file_stream)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())

print("\nDist1: ")
print(dist1)
