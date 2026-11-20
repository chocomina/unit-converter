import math
import time
"""unit converter"""
cat = ("which category would you like to convert? we support length(1), weight(2) and temperature(3):") 
if cat == ("1"):
    unit1 = ("what unit would you like to convert from:")
    unit2 =  ("what unit would you like to convert to:")
    num1 =  ("enter your value:")

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
        ans = float(num1) *1000
    elif unit1 == "m" and unit2 ==("km"):
        ans = float(num1)/1000
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1)/1000000
    elif unit1 == "km" and unit2 == "mm":
        ans = float(num1)*1000000
    elif unit1 == "cm" and unit2 == "km":
        ans = float(num1)/100000    
    elif unit1 == "km" and unit2 == "cm":
        ans = float(num1)*100000 



    if cat == ("2"):
        unit1 = ("what unit would you like to convert from:")
        unit2 =  ("what unit would you like to convert to:")
        num1 =  ("enter your value:")

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



            if cat == ("3"):
                unit1 = ("what unit would you like to convert from:")
                unit2 =  ("what unit would you like to convert to:")
                num1 =  ("enter your value:")

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


                    