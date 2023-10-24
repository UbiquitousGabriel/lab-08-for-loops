highestNum = 0
# initiate highestnum variable as 05
# we will replace this 0 in our loop

for answer in range(0, 4, 1):
    userInput = input("Number please...")
    userInt = int(userInput)
    print("User entered:" + str(userInput))
    if userInt > highestNum:
        highestNum = userInt
        print("Updating highest number...")
    else:
        print("This is not the highest number!")