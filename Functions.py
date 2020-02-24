
def add(x, y):
    n1 = int(x)
    n2 = int(y)
    return n1 + n2

def subtract(x, y):
    return int(x) - int(y)


def do_math(operation, operand1, operand2):
    if operation == "+":
        return add(operand1, operand2)
    elif operation == "-":
        return subtract(operand1, operand2)
    else:
        print(f'{operation} is not a supported operation.')
    return None

print("Starting ....")
op = input("Please enter an operation to do: ")
op1 = input("Please enter first operand: ")
op2 = input("Please enter two operand: ")

result = do_math(op, op1, op2)
if result is not None:
    print(f'{op1} {op} {op2} == {result}')
