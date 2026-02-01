import random
while True:
    try:
        num1 = int(input("Enter a lower bound number: "))
        num2 = int(input("Enter a higher bound number: "))

        if num1 == num2:
            print("Please enter different numbers.")
            continue
        if num1 > num2:
            print("Please enter lower bound number first.")
            continue

        break
    except ValueError:
        print("Please enter a number.")


Lower = min(num1, num2)
Upper = max(num1, num2)

random_number = random.randint(Lower, Upper)
print(random_number)

