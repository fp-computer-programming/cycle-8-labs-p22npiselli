# Author: Nolan (AMDG) 12/3/2021

total = 0
while True:
    user_number = input("Enter a number: ")
    if user_number == "-1":
        break
    else:
        total += int(user_number)

print("The sum of all the numbers entered is {0}".format(total))


    