number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your first number: "))

while(number_2):
    numbers = number_2
    number_2 = number_1 % number_2
    number_1 = numbers

print("The HCF of your two numbers is: ", number_1)