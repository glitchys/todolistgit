password = input("Enter a Password:")

result = {}

if len(password) >= 8:
    result["Length:"] = True
else:
    result["Length:"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digits: "] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["Uppercase: "] = uppercase

print(result)
if all(result.values()) == True:
    print("Strong Password")
else :
    print("Weak Password")