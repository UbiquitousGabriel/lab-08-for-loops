sum = 0
avg = 0
for numUp in range(4):
    uInput = input("Enter a number:")
    sum = sum + int(uInput)

avg = sum/4;
print("The average is: " + str(avg))