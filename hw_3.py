import math
import random


#1.1
number = abs(int(input("Enter the number: "))) # будь-яке ціле число
sum = 0
if number == 0:
        print("Sum:", number)
else:
    first_two_digit = number // 10 # знаходимо перші дві цифри
    first_digit = first_two_digit // 10 # знаходимо першу цифру - ціле від ділення 
    second_digit = first_two_digit % 10 # знаходимо другу цифру - частка від ділення
    last_digit = number % 10 # знаходимо останню цифру - частка від ділення 
    sum = first_digit + second_digit + last_digit
#     number = number // 10
print("Sum: ", sum)

#1.2
number = abs(int(input("Enter the number: "))) # будь-яке ціле число
sum = 0
while (number > 0):
    if number == 0:
        print("Sum:", number)
    else:
        digit = number % 10
        sum = sum + digit 
        number = number // 10
print("Sum: ", sum)


#2
number = abs(float(input("Enter the number: ")))

print(int(number * 10) % 10)

# 3 варінта які виводять не точну відповідь 
print("Digit: ", number % 1)
print(math.modf(number))
print(number - int(number))

#4
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for i in list_of_six:
    if i % 5 == 0 and i < 150:
        print(i) 


#5
for i in range(1, 4):
    if 1<= i <= 3:
        input_number = int(input("Enter the number: "))
        number_of_try = 1
        random_number_1 = random.randint(1, 10)
        print("First nuber is: ", random_number_1)
        random_number_2 = random.randint(1, 10)
        print("Second nuber is: ", random_number_2)
        random_number_3 = random.randint(1, 10)
        print("Third nuber is: ", random_number_3)
        if input_number == random_number_1 or input_number == random_number_2 or input_number == random_number_3:
            print("You won!!!")
            break
        else:
            print("You lose")


#6
x = int(input("Enter the x (1-2): "))
y = int(input("Enter the y (1-2): "))


if 0 < x <= 2 and 0 < y <= 2:
    if x == 2 and y == 1 or x == 1 and y == 2:
        print("Player can make this step")
else:
    print("Player can not make this step")


#7
number = int(input("Enter the number to calculate the factorial: "))
factorial = 1

for i in range(2, number + 1):
    factorial *= i
print(factorial)