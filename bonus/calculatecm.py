feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
   parts = feet_inches.split(" ")
   feet = float(parts[0])
   inches = float(parts[1])
   meter = feet * 30.48 + inches * 2.54
   return meter

result = convert(feet_inches)

if result < 1:
    print("Too small.")
else:
    print("Good.")