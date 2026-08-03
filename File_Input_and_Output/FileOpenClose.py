my_file = open('test.txt')

print(my_file.readline()) # read only line by line subsequent calls to readline() will read the next line in the file
my_file.seek(0)  # Move the cursor back to the beginning of the file    
print(my_file.read())

# or 
my_file.seek(0)
print(my_file.readlines()) # read all lines in the file and return them as a list of strings

my_file.close() # close the file after reading