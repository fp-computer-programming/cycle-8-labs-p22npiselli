# Author: Nolan (AMDG) 12/2/2021

def sum_to(n):
    total = 0
    x = 0
    while x <= int(n):
        print(total)
        total += 1
        x += 1
        return total

n = input("Enter a number: ")
print(sum_to(n))
        
    