# -*- coding: utf-8 -*-

#Suchit Mudichintala
#CS175

#Sets

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Display members of the baseball team
print("The following students are on the baseball team:")
for member in baseball:
    print(member)

# Display members of the basketball team
print("\nThe following students are on the basketball team:")
for member in basketball:
    print(member)

# Display students who play both baseball and basketball (intersection)
both_sports = baseball & basketball
print("\nThe following students play both baseball and basketball:")
for member in both_sports:
    print(member)

# Display students who play either baseball or basketball (union)
either_sport = baseball | basketball
print("\nThe following students play both baseball or basketball:")
for member in either_sport:
    print(member)

# Display students who play baseball but not basketball (difference)
baseball_not_basketball = baseball - basketball
print("\nThe following students play baseball, but not basketball:")
for member in baseball_not_basketball:
    print(member)

# Display students who play basketball but not baseball (difference)
basketball_not_baseball = basketball - baseball
print("\nThe following students play basketball but not baseball:")
for member in basketball_not_baseball:
    print(member)

# Display students who play one sport, but not both (symmetric difference)
one_sport = baseball ^ basketball
print("\nThe following students play one sport, but not both:")
for member in one_sport:
    print(member)

#Dictionaries

#Q1. Create a program that will print only the names of the people who live in Chicago. Use a list comprehension.


persons = {'Danny': 'New York', 'Ben': 'New Jersey', 'Bob': 'Chicago', 'Tom': 'Houston', 'Sam': 'Phoenix', 'Tim': 'Philadelphia', 'Nancy': 'Chicago'}


chicago_residents = [person for person, city in persons.items() if city == 'Chicago']

# Print the result as a list
print(chicago_residents)

#Q2. Given a dictionary, create a new dictionary where keys and values are swapped.

original = {'Math':'Alice', 'Science':'Bob', 'History': 'Charlie'}

swapped = {value: key for key, value in original.items()}

# Print the result as a dictionary
print(swapped)

#Q3. Create a program to select only employees in the Sales department in this nested dictionaries; you can filter based on certain conditions within the inner dictionaries.

employees = {'Alice': {'age': 25, 'department': 'Sales'},
             'Bob': {'age': 30, 'department': 'Marketing'},
             'Charlie': {'age': 28, 'department': 'Sales'},
             'Daisy': {'age': 22, 'department': 'IT'}}

sales_employees = {name: info for name, info in employees.items() if info['department'] == 'Sales'}

print(sales_employees)

#Q4. Create a program to combine Two Dictionaries, summing values for Common Keys.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 50}

combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

print(combined_dict)

#Q5. Create a program to store friend’s name and birthdate in a dictionary object using input().Also, ensures the birthday is entered in the correct YYYY-MM-DD format.
#Create another program to view specific friend’s name and birthdate.
#Create the main_menu() program that Offers a menu to let the user add, view, or exit. The main_menu() function manages the program flow.

from datetime import datetime

def add_friend(birthday_book):
    name = input("Enter friend's name: ").strip()
    while True:
        birthdate = input("Enter birthday (e.g., YYYY-MM-DD): ").strip()
        try:
            # Validate date format
            datetime.strptime(birthdate, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    birthday_book[name] = birthdate
    print(f"{name}'s birthday has been added!")

def view_friend(birthday_book):
    name = input("Enter the name of the friend whose birthday you want to view: ").strip()
    if name in birthday_book:
        print(f"{name}'s birthday is on: {birthday_book[name]}")
    else:
        print(f"{name} is not in the birthday book.")

def view_all_birthdays(birthday_book):
    if birthday_book:
        print("\nFriends' Birthdays:")
        for name, birthdate in birthday_book.items():
            print(f"{name}: {birthdate}")
    else:
        print("\nNo birthdays have been added yet.")

def main_menu():
    birthday_book = {}
    while True:
        print("\nBirthday Manager")
        print("1. Add a Birthday")
        print("2. View a Birthday")
        print("3. Display All birthdays")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_friend(birthday_book)
        elif choice == '2':
            view_friend(birthday_book)
        elif choice == '3':
            view_all_birthdays(birthday_book)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the main menu
main_menu()
