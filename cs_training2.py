from cs_training1 import pow

def operation(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "x":
        return n1 * n2
    elif op == "÷":
        return n1 / n2
    elif  op == "pow":
        return pow(n1, n2)
    else:
        return "Invalid operation, try again."
    
def roundop(result):
        if result.is_integer():
            return int(result)
        else:
            return result

# functions that will be useful in the future

n1 = float(input("Pick a random number:"))
op = input("Pick an operation: +, -, x, ÷ or pow (for power):")
n2 = float(input("Pick another random number:"))

# user's area

result = operation(n1, n2, op)
result = roundop(result)

# calling and storing the functions

print(f"{n1} {op} {n2} ={result}")
