#with open('test.txt', mode = 'w') as my_file: 
 #   text = my_file.write(':)')
   # print(text)

try: 
    with open('sad.txt', mode = 'r') as my_file: 
    # text = my_file.write(':(')
        print(my_file.read())

except FileNotFoundError as err:
    print("File not found error: ")
    raise err

except IOError as err:
    print("io error: ")
    raise err