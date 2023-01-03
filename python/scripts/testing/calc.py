""" calc module """
def add(x: int, y: int) -> int:
    """ Compute the sum of two numbers 
    Parameters
    x : int
        First operand
    y : int
        Second operand

    Returns
    int
        Sum of the two operands
    """
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y





# print(add(4,5)) # => 9