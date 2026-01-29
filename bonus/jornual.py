date = input("Enter today's date: ")
mood = input("Enter mood level from 1 to 10: ")
thoughts = input("Write down your thoughts:\n ")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)

