
####3#my method
#with open('Coding_Exercise_1.txt',  'r') as file:
#    print(file.seek(4))
#    print(file.read(5))
#file.close()

#udemy method
f = open('Coding_Exercise_1.txt', 'r')
f.seek(4)
word = f.read(5)
print(word)
f.close()