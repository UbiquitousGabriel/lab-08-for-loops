for listedNum in range(1,101):
    if listedNum %3 == 0:
        print("Fizz..")
    elif listedNum %5 == 0:
        print("Buzz..")
    else:
        print(str(listedNum))