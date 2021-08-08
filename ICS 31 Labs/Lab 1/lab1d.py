# Raul Cervantes 77825705 and Emmanuel Ezenwa Jr. 44756552. ICS 31 Lab sec 3
def factorial (n: int) -> int:
    '''Compute n! (n factorial)'''
    if n <= 0:
        return 1
    else:
        return n * factorial(n -1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(120))
print("100! is", factorial(factorial(5)))