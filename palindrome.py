str_a = input()
if len(str_a) < 0:
    print("Invalid string")
else:
    reverse = str_a[::-1]
if str_a == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
