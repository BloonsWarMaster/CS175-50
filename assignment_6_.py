# -*- coding: utf-8 -*-
"""Assignment 6 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ip7hl-a98fkFcu7-7hx5eGTBe6FfN3cw
"""

#Suchit Mudichintala
#CS 175

#create numbers file

def main():

  outfile = open('numbers.txt', 'w')

  outfile.write('1\n')
  outfile.write('2\n')
  outfile.write('3\n')

  outfile.close()

if __name__ == '__main__':
  main()

#Average From Input File with Exception Handling

def main():
    filename = 'numbers.txt'

    try:
        values = get_Value(filename)
        if not values:
            raise ValueError("The file does not contain any valid numbers")

        avg = get_avg(values)

        print_avg(avg)

    except IOError:
        print(f"Error: Could not open the file '{filename}'")
    except ValueError as e:
        print(f"Error: {e}")


def get_Value(filename):

    with open(filename, 'r') as infile:
        return [float(line.strip()) for line in infile]


def get_avg(values):

    if len(values) == 0:
        raise ValueError("No valid numbers to calculate an average.")

    return sum(values) / len(values)

def print_avg(avg):

    print(f"The average of the numbers is {avg:.2f}")


if __name__ == '__main__':
    main()

#Read a file to add numbers and display total

def main():
    filename = 'numbers.txt'
    numbers = []

    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            numbers.append(number)

    num1 = numbers[0]
    num2 = numbers[1]
    num3 = numbers[2]

    total = num1 + num2 + num3

    print(f"The numbers are: {num1}, {num2}, {num3}")
    print(f"Their total is: {total}")

if __name__ == '__main__':
    main()

#Create records in employees.txt

def main():
  num_emps = int(input('How many employees will be entered? '))

  emp_file = open('employees.txt', 'w')

  for count in range(1, num_emps + 1):
    print(f'Enter data for employee #{count}')

    name = input('Name: ')
    id_num = input('ID number: ')
    dept = input('Department: ')

    emp_file.write(f'{name}\n')
    emp_file.write(f'{id_num}\n')
    emp_file.write(f'{dept}\n')

    print()

  emp_file.close()
  print('Employee records written to employees.txt')

if __name__ == '__main__':
    main()

#Search records in employees.txt

def main():
    try:
        search_name = input('Enter a name to search for: ')
        found = False

        emp_file = open('employees.txt', 'r')

        name = emp_file.readline()

        while name != '' and not found:
            id_num = emp_file.readline()
            dept = emp_file.readline()

            name = name.rstrip('\n')
            id_num = id_num.rstrip('\n')
            dept = dept.rstrip('\n')

            if name == search_name:
                print(f'Name: {name}')
                print(f'ID number: {id_num}')
                print(f'Department: {dept}')
                found = True

            name = emp_file.readline()

        emp_file.close()

        if not found:
            print(f'That record was not found in the file.')

    except FileNotFoundError:
        print('Error: The file employees.txt was not found.')

if __name__ == '__main__':
    main()

#Try-except blocks

def main():
    filename = 'employees.txt'
    search_term = input("Enter a search term: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

            if search_term not in content:
                raise Exception(f"'{search_term}' not found in the file.")

            print(f"'{search_term}' was found in the file.")

    except FileNotFoundError:
        print(f"'{filename}' does not exist.")
    except IsADirectoryError:
        print(f"'{filename}' is a directory, not a file.")
    except Exception as e:
        print(f"{e}")

if __name__ == '__main__':
    main()