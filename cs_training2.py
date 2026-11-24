from cs_training1 import pow
from cs_training1 import operation
from cs_training1 import roundop
import sys

#importing the functions from the previows file.

n1 = float(input("Pick a random number:"))
op = input("Pick an operation: +, -, x, ÷ or pow (for power):").strip()
n2 = float(input("Pick another random number:"))

#storing the user's answers in variables.

result = operation(n1, n2, op)
result = roundop(result)

#calling and storing the functions

print(f"{n1} {op} {n2} ={result}")

keep = input("Continue?").strip().lower()

while keep == "yes" or keep == "y" or keep == "ye" or keep == "yeah":
    n1 = float(input("Pick a random number:"))
    op = input("Pick an operation: +, -, x, ÷ or pow (for power):").strip()
    n2 = float(input("Pick another random number:"))
    result = operation(n1, n2, op)
    result = roundop(result)
    print(f"{n1} {op} {n2} ={result}")
    keep = input("continue?").strip().lower()
else:
    print("Thanks for using the calculator!")