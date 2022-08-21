#f = open('configuration.txt', 'r')
#content = f.read(7)
#print(content)

#print(f.tell()) # shwo the cursur position
#print(f.seek(2)) # moving the cursur to position index 2
#print(f.read(3))
#print(f.close)

#using with
with open('configuration.txt', 'r') as file:
    print(file.read())
print(file.close)