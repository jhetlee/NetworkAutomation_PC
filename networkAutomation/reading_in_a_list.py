with open('configuration.txt') as file:
    my_list = file.read().splitlines()
    print(my_list)

with open('configuration.txt', 'r') as file1:
    my_list1 = file1.readlines()
    print(my_list1)

with open('configuration.txt', 'r') as file2:
    print(file2.readline())
    print(file2.readline())

with open('configuration.txt', 'r') as file2:
    for line in file2:
        print(line, end='') # end='' use to remove spaces