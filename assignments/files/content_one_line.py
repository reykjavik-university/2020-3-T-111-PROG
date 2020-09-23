def open_file(filename):
  ''' Opens the given file and returns the corresponding file object '''
  file_object = open(filename, 'r')
  return file_object

def process_file(file_object):  
  '''Reads the given file_object and returns its contents in a single string after removing white spaces'''
  line_str = ""

  for line in file_object:
    line = line.strip()
    line = line.replace(" ", "")
    line_str += line
  
  return line_str

# Main starts here
file_name = input("Enter filename: ")
file_object = open_file(file_name)
single_line = process_file(file_object)
print(single_line)
file_object.close()