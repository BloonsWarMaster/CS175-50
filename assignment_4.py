# -*- coding: utf-8 -*-

# CS 175
# Suchit Mudichintala
# four_digits.py

valid_input = False

while not valid_input:
    four_digit_num = int(input("Enter a four digit integer: "))

    if 1000 <= four_digit_num <= 9999:

        valid_input = True

        digit_1 = four_digit_num // 1000
        digit_2 = (four_digit_num // 100) % 10
        digit_3 = (four_digit_num // 10) % 10
        digit_4 = four_digit_num % 10

        sum_digits = digit_1 + digit_2 + digit_3 + digit_4

        print("The individual digits of your input are:", digit_1, digit_2, digit_3, digit_4)
        print("The sum of your input is:", sum_digits)

    else:
        print("Invalid input. Please enter a four-digit integer.")

# CS 175
# Suchit Mudichintala
# commissions

another_commission = "yes"

while another_commission.lower() == "yes":
  sale = float(input("Enter your sale: $"))

  commission_rate = float(input("Enter the commission rate(in %): "))
  commission = (commission_rate/100) * sale

  print(f"The commission is: ${commission:.2f}")

  another_commission = input("Do you want to do another sale commission? ")

#CS 175
#Suchit Mudichintala
#for loop


#Squares of List Elements

list = [2,4,6,8]

for num in list:
  print(num**2, end = " ")
print()
print()


#Grade Calculator

marks = [85, 92, 78, 90, 88]

total = 0
for num in marks:
  total = num + total

avg = total / len(marks)

if avg >= 90:
  print("Your grade is A.")
elif avg >= 80:
  print("Your grade is B.")
elif avg >= 70:
  print("Your grade is C.")
elif avg >=60:
  print("Your grade is D.")
else:
  print("Your grade is F.")

#CS 175
#Suchit Mudichintala
#Asignments with for loop

#1.

str = input("Input a string: ").lower()

vowels = "aeiou"
count = 0

for char in str:
  if char in vowels:
    count = count + 1

print("Number of vowels:", count)

#2

num = int(input("Enter a number: "))

for i in range(11):
  product = num*i
  print(f"{num} x {i} = {product}")

#3

student_grades = {
    	"Alice": 85,
    	"Bob": 92,
    	"Charlie": 78,
    	"Diana": 88,
    	"Eve": 91
	}

for student in student_grades:

  grade = student_grades[student]
  print(f"{student}: {grade}")

#4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

even_list = []
odd_list = []


for num in numbers:
  if num % 2 == 0:
    even_count += 1
    even_list.append(num)
  else:
    odd_count +=1
    odd_list.append(num)

print(f"There are {even_count} even numbers in the list.")
print(f"There are {odd_count} odd numbers in the list.")
print(f"List of even numbers: {even_list}")
print(f"List of odd numbers: {odd_list}")

#5

numbers = [3, 5, 7, 2, 8, -1, 4]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num
  if num < smallest:
    smallest = num

print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")
