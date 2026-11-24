import sys
def pow(n1, n2):
    return n1 ** n2


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
        print("Invalid operation.")
        sys.exit()

def roundop(result):
        if result.is_integer():
            return int(result)
        else:
            return result
        