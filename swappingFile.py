def swapFileData():
    userInputA = input("Enter the name of the file ")
    userInputB = input("Enter the name of the second file ")
    with open(userInputA, 'r') as a:
        data_a = a.read()
    with open(userInputB, 'r') as b:
        data_b = b.read()
    with open(userInputA, 'w') as a:
        a.write(data_b)
    with open(userInputB, 'w') as b:
        b.write(data_a)
swapFileData()