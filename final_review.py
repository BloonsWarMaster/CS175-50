# -*- coding: utf-8 -*-

#Suchit Mudichintala
#CS 175

#Q1. Type the lines of code that calls the split method to print only the year part of the variable "date_string"

date_string = '11/26/2020'

final = date_string.split('/')
print(final[2])

#Q2: Create a program to multiply each element of 'a' with the corresponding element in 'b' and sum the result. If an element in a is 0, we skip that element.
#use continue statement to skip multiplication if an element in a is 0.
#For each other element, x is multiplied by the corresponding element in b, and the result is added to total.

a = [1, 2, 0, 1]
b = [3, 4, 6, 5]
total = 0
for x in a:
  if x == 0:
    continue

  total += x * b[a.index(x)]

print(total)

#Q3: Create a program to count the occurrences of each word in a sentence.

sentence = "apple banana apple orange banana apple"
words = sentence.split()
word_count = {}

for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)

#Q4. Create a program to replace all vowels in a string with the @ character.

text = "Hello, World!"
vowels = "aeiouAEIOU"

for char in text:
  if char in vowels:
    text = text.replace(char, "@")

print(text)

#Q5. Create a program to capitalize the first letter of each word in a sentence.

sentence = "it's raining cats and dogs."
words = sentence.split()
capitalized_words = []

for word in words:
  capitalized_words.append(word.capitalize())

capitalized_sentence = " ".join(capitalized_words)

print(capitalized_sentence)

#Q6. Create a program to find the longest word in a given sentence.

sentence = "Chicago is very different from Boston"
words = sentence.split()
longest_word = ""

for word in words:
  if len(word) > len(longest_word):
    longest_word = word

print(longest_word)

#Q7. Create a program to remove all numeric characters from a string.

text = "Python 3.9 is great for 2024!"
result = ""

for char in text:
  if not char.isdigit():
    result += char

print(result)

#Q8. Create a program to count the number of uppercase letters, lowercase letters, and digits in a string.

text = "Hello World! Python3"
uppercase_count = 0
lowercase_count = 0
digit_count = 0

for char in text:
  if char.isupper():
    uppercase_count += 1
  elif char.islower():
    lowercase_count += 1
  elif char.isdigit():
    digit_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)

#Q9. Create a program to check if two strings are anagrams of each other (contain the same characters in a different order).

string1 = "listen"
string2 = "silent"

if sorted(string1) == sorted(string2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")

#Q10. Create a program to track the stock of items in a store and updates the inventory when items are sold.

# Initial inventory
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

# List of items sold
sold_items = ["apple", "banana", "grape", "apple", "orange", "banana"]

for item in sold_items:
  if item in inventory:
    inventory[item] -= 1

print(inventory)

#Q11. Suppose the file “sample.txt” exists on your computer. What will be printed in the console if you run the below code and enter “sample.txt” as input?

# The file 'sample.txt' has 1 lines.

#Q12. Suppose the file “numbers.txt” exists on your computer. What will be printed in the console if you run the below code and enter “numbers.txt” as input?

# An unexpected error occured: could not convert string to float: 'abc'

#Q13. Suppose the file “numbers.txt” exists on your computer. What will be printed in the console if you run the below code and enter “numbers.txt” as input?

# Invalid data found: 'abc'. Skipping this line.
# The total sum of numbers in the file is: 60.0
