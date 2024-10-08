# -*- coding: utf-8 -*-

#CS 175
#Suchit Mudichintala
#Modular Program

def get_grade():
  grade = int(input("Enter a grade between 0 and 100: "))
  return grade

def letter_grade(percentage_grade):
  if percentage_grade >= 90:
    print("You passed with an A")
  elif percentage_grade >= 80:
    print("You passed with a B")
  elif percentage_grade >= 70:
    print("You passed with a C")
  elif percentage_grade >= 60:
    print("You passed with a D")
  else:
    print("You failed with an F")

def main():
  grade_1 = get_grade()
  grade_2 = get_grade()
  grade_3 = get_grade()
  final_grade = (grade_1 + grade_2 + grade_3) / 3
  print("Your final grade percentage is", final_grade)
  letter_grade(final_grade)

main()

#Temperature Conversion

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def main():

  user_input = int(input("'1' to convert Celsius to Fahrenheit or '2' to convert Fahrenheit to Celsius: "))

  if user_input == 1:
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
  elif user_input == 2:
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")

main()

#Extract First Name

def extract_first_name(full_name):
  first_name = full_name.split()
  return first_name[0]

def main():
  full_name = input("Please enter your full name: ")
  first_name = extract_first_name(full_name)
  print("Your first name is:", first_name)

main()

#Remove Empty String

def remove_empty_strings(string_list):
  new_list = []
  for string in string_list:
    if string.strip() != "":
      new_list.append(string)
  return new_list

def main():
  string_list = ["", "   a    ", "b", " ", "c    "]
  new_list = remove_empty_strings(string_list)
  print(new_list)

main()

#Calculate a person's weekly pay

def get_input():
    wage = float(input("Please enter wage: "))
    hours_worked = float(input("Please enter hours worked: "))
    return hours_worked, wage

def weekly_pay(hours_worked, wage):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (wage * 1.5)
        regular_pay = 40 * wage
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours_worked * wage
    return total_pay

def main():
    hours_worked, wage = get_input()
    total_pay = weekly_pay(hours_worked, wage)
    print("Weekly pay: $", total_pay)

main()

#Nested loop

outer_loop = int(input("Enter range of outside loop: "))
inside = 4
total = 0
total_cycles = 0

for x in range(outer_loop):
    print(f"Outer loop value: {x + 1}")

    for y in range(inside):
        value = int(input(f"Enter something: "))
        total += value
        total_cycles += 1

print(f"Total cycles: {total_cycles}")
print(f"Total: {total}")
