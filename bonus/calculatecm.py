from bonus.converters import convert
from bonus.parsers import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} meters.")


if result < 1:
    print("Too small.")
else:
    print("Good.")