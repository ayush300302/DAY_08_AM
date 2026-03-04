\# PAN Card Validation using Python



\## Exact Prompt Used



"Write a Python program that validates an Indian PAN card number format using if-else conditions.

PAN format: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F).

The 4th character indicates the type of taxpayer."



---



\# AI Generated Code



```python

pan = input("Enter PAN number: ")



if len(pan) == 10:

&nbsp;   

&nbsp;   if pan\[:5].isalpha() and pan\[:5].isupper():

&nbsp;       

&nbsp;       if pan\[5:9].isdigit():

&nbsp;           

&nbsp;           if pan\[9].isalpha() and pan\[9].isupper():

&nbsp;               print("Valid PAN number")

&nbsp;           else:

&nbsp;               print("Invalid PAN format")

&nbsp;               

&nbsp;       else:

&nbsp;           print("Digits expected in positions 6-9")

&nbsp;           

&nbsp;   else:

&nbsp;       print("First five characters must be uppercase letters")

&nbsp;       

else:

&nbsp;   print("PAN must be 10 characters long")

