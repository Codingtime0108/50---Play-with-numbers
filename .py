number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

a = number_1
b = number_2

while(b):
    numbers = b
    b = a % b
    a = numbers

hcf = number_1

lcm = (number_1 * number_2)//hcf

print("LCM is:",lcm)