#with open('configuration.txt', 'w') as f:
 #   f.write('just a line\n')
 #   f.write('just a second line')
#note if the file is existing ex: configuration.txt it will be overwritten

with open('configuration.txt', 'r+') as file: # "r+" used for reading and writing files and files must be existing else it will receive an error
    file.seek(5)
    file.write('100\n')
    file.seek(10)
    print(file.read(7))
