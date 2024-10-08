# -*- coding: utf-8 -*-
"""Assignment 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w6jTif7D3Xr7mg4ZcCMaLgXGRyDIn4H8
"""

# stocks
# Suchit Mudichintala

#Constants
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75


#Declare variables
amountPaidForStock = 0

purchaseCommission = 0

totalPaid = 0

stockSoldFor = 0

sellingCommission = 0

totalReceived = 0

profitOrLoss = 0


#Set variables
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

purchaseCommission = COMMISSION_RATE * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

stockSoldFor = NUM_SHARES * SELLING_PRICE

sellingCommission = COMMISSION_RATE * stockSoldFor

totalReceived = stockSoldFor - sellingCommission

profitOrLoss = totalReceived - totalPaid


#Display
print(f"Amount paid for stock: ${amountPaidForStock}")
print(f"Commission paid on the purchase: ${purchaseCommission}")
print(f"Amount the stock sold for: ${stockSoldFor}")
print(f"Commission paid on the sale: ${sellingCommission}")
print(f"Profit(or loss if negative): ${profitOrLoss}")

# name_printer
# Suchit Mudichintala

name = "Suchit"

border = "+------+"

middle = "|" + name + "|"

print(border)
print(middle)
print(border)

# account_balance
# Suchit Mudichintala

INTEREST_RATE = 0.005

initBalance = 1000

firstYear = initBalance * (1 + INTEREST_RATE)
secondYear = firstYear * (1 + INTEREST_RATE)
thirdYear = secondYear * (1 + INTEREST_RATE)

print(f"Balance after first year: ${firstYear:,.2f}")
print(f"Balance after second year: ${secondYear:,.2f}")
print(f"Balance after third year: ${thirdYear:,.2f}")

# math_ops
# Suchit Mudichintala


num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

sum = num1 + num2

difference = num1 - num2

product = num1 * num2

average = (num1 + num2) / 2

distance = abs(difference)

maximum = max(num1, num2)

minimum = min(num1, num2)

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Average: {average}")
print(f"Distance: {distance}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

# f_to_c_.py
# Suchit Mudichintala

F = int(input("Enter temperature in Fahrenheit: "))

#convert Fahrenheit to Celsius
C = (F-32)*(5/9)

print(f"Temperature in Celsius: {C}")

# format_print.py
# Suchit Mudichintala

num1 = 1.8
num2 = 12.9
num3 = 2
num4 = 100.25

print(f"{num1:.2f}\n{num2:.2f}\n{num3:.2f}\n{num4:.2f}")

# print_grid.py
# Suchit Mudichintala

var1 = "+--+--+--+\n|  |  |  |"
var2 = "+--+--+--+"

print(var1)
print(var1)
print(var1)
print(var2)

#format output exercise
#Suchit Mudichintala

var1 = int(input("Enter first integer: "))
var2 = int(input("Enter second integer: "))


fsum = "Sum:"
sum = var1 + var2

fdifference = "Difference:"
difference = var1 - var2

fproduct = "Product:"
product = var1 * var2

fintDivision = "Integer Division:"
intDivision = var1//var2

faverage = "Average:"
average = (var1+var2)/2

fremainder = "Remainder:"
remainder = (var1 % var2)

fexponent = "Exponent:"
exponent = var1**var2

print()
print(f"{fsum:<19}",f"{sum:>15.2f}")
print(f"{fdifference:<19}",f"{difference:>15.2f}")
print(f"{fproduct:<19}",f"{product:>15.2f}")
print(f"{fintDivision:<19}",f"{intDivision:>15.2f}")
print(f"{faverage:<19}",f"{average:>15.2f}")
print(f"{fremainder:<19}",f"{remainder:>15.2f}")
print(f"{fexponent:<19}",f"{exponent:>15.2f}")