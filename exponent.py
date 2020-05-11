def exponent(num, power=2):
    """Exponent(num, power) raises num to specified power. Power defaults to 2."""
    return num ** power

print(exponent(2,3))
print(exponent(3))
print(exponent(7))


print(exponent(power=3, num=4))

print(exponent.__doc__)
