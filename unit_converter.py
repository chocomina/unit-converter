import math
import time
"""unit converter"""
cat = input("which category would you like to convert? we support length(1), weight(2) and temperature(3):")

if cat == "1":
    unit1 = input("what unit would you like to convert from:").strip().lower()
    unit2 = input("what unit would you like to convert to:").strip().lower()
    num1 = input("enter your value:")

    ans = None
    if unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1)*100
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1)*10
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1)/1000
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1)*1000
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1)*1000
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1)/1000
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1)/1000000
    elif unit1 == "km" and unit2 == "mm":
        ans = float(num1)*1000000
    elif unit1 == "cm" and unit2 == "km":
        ans = float(num1)/100000
    elif unit1 == "km" and unit2 == "cm":
        ans = float(num1)*100000

    if ans is None:
        print("sorry, i dont know dat convo")
    else:
        print(num1, unit1, "=", ans, unit2)

elif cat == "2":
    unit1 = input("what unit would you like to convert from:").strip().lower()
    unit2 = input("what unit would you like to convert to:").strip().lower()
    num1 = input("enter your value:")

    ans = None
    if unit1 == "kg" and unit2 == "g":
        ans = float(num1)*1000
    elif unit1 == "g" and unit2 == "kg":
        ans = float(num1)/1000
    elif unit1 == "mg" and unit2 == "g":
        ans = float(num1)/1000
    elif unit1 == "g" and unit2 == "mg":
        ans = float(num1)*1000
    elif unit1 == "kg" and unit2 == "mg":
        ans = float(num1)*1000000
    elif unit1 == "mg" and unit2 == "kg":
        ans = float(num1)/1000000

    if ans is None:
        print("sorry, i dont know dat convo")
    else:
        print(num1, unit1, "=", ans, unit2)

elif cat == "3":
    unit1 = input("what unit would you like to convert from:").strip().lower()
    unit2 = input("what unit would you like to convert to:").strip().lower()
    num1 = input("enter your value:")

    ans = None
    if unit1 == "c" and unit2 == "f":
        ans = (float(num1)*9/5)+32
    elif unit1 == "f" and unit2 == "c":
        ans = (float(num1)-32)*5/9
    elif unit1 == "c" and unit2 == "k":
        ans = float(num1)+273.15
    elif unit1 == "k" and unit2 == "c":
        ans = float(num1)-273.15
    elif unit1 == "f" and unit2 == "k":
        ans = (float(num1)-32)*5/9+273.15
    elif unit1 == "k" and unit2 == "f":
        ans = (float(num1)-273.15)*9/5+32

    if ans is None:
        print("sorry, what u talm bout?")
    else:
        print(num1, unit1, "=", ans, unit2)

else:
    print("only 1 or 2 or 3 idiot")
