# שאלה1
# for i in range(1001):
#     if i%3==0 and i%5==0:
#         print("fuzzbuzz")
#     elif i%3==0:
#         print("fuzz")
#     elif i%5==0:
#         print("buzz")
#     else:print(i)
# from unicodedata import numeric
from itertools import count

from unicodedata import digit

# שאלה2
# num = int(input("please enter a number"))
# for i in range(1,num+1):
#     print("*" * i)
# while 0<i:
#     i-=1
#     print("*"*i)

# for i in range(4,0,-1):
#     print("*"*i) num=int(input("please enter a number:"))
#


# שאלה# 3
# x=True
# num=int(input("please enter a natural number:"))
# for i in range(2,num):
#    if num%i==0:
#         x=False
# if x:
#     print(num,"This number is a prime number")
# else:
#     print(num,"This number is not a prime number")

# שאלה 4

# num = int(input("please enter a number:"))
# for i in range(1, num + 1):
#     x=" " * (num -i)
#     print(x,f"{i} "* i)

# שאלה 5
# num = int(input("please enter your number:"))
# copy_num = num
# revers_number = 0
# while num > 0:
#     ahdot = num % 10
#     num = num // 10
#     revers_number += ahdot
#     revers_number *= 10
# revers_number //= 10
# if revers_number == copy_num:
#     print(copy_num, "is pallindrom")
# else:
#     print(copy_num, "is not pallindrom")


# שאלה6
x = True

sum_ = 0
even_number_count = 0
odd_number_count = 0
min_val =0
max_val = 0
while x:
    num = (input("please enter a number to exit precede exit:"))

    min_val=num
    if num in str("exit"):
        if even_number_count + odd_number_count == 0:
            print("you can't exit before you enter least one value ")
        else:
            print("count is  ", even_number_count + odd_number_count,
                  "even num is ", even_number_count, "odd num is", odd_number_count,
                  "min value is ", min_val, ", max value is ", max_val,
                  "avg value is ", sum_ / (even_number_count + odd_number_count)
                  )
            x = False
    else:
        num = int(num)
        sum_ += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        if num % 2 == 0:
            even_number_count += 1
        else:
            odd_number_count += 1

# שאלה8
# num = int(input("please enter your number:"))
# num1 = 1
# num2 = 1
# print(num1, num2, end=" ")
# for i in range(3, num + 1):
#     temp = num1 + num2
#     print(temp, end=" ")
#     num1 = num2
#     num2 = temp

# שאלה 7
# Create_a_user =0
# pasword =0
# x = True
# while x:
#     user = input("a,login\nb,Create a user\nc,logout \n"
#                  "d,Back to the main menu \nChoose one from a,b,c,d:")
#     if user=="b":
#
#
#
#     if user == "a":
#         user_name = input("please enter a user name or Press asterisk to return to the main menu:")
#         import re
#
#         while True:
#             Create_pasword = input("enter your pasword (must include letters and numbers) or Press asterisk to return to the main menu:")
#             if re.search("[A-Za-z]", Create_pasword) and re.search("[0-9]", Create_pasword):
#                 if user_name == Create_a_user and Create_pasword == pasword and Create_pasword or user_name != "*":
#                     print("'Welcome to my project'")
#                     user_a = input("Choose one from a,b,c,d \n a,chang pasword \n"
#                                " b,remove a user \n c,return to the main menu \n d,logout:")
#                     if user_a == "a":
#                         old_pasword =input("enter your old pasword:")
#                         if old_pasword==Create_pasword:
#                             new_pasword=input("create new pasword (must include letters and numbers):")
#                             Create_pasword=new_pasword


