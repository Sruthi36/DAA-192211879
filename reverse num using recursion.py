def reverse_num(number):
    if number  == 0:
        return ""
    else:
        return str(number% 10) + str(reverse_num(number //10))
number = 258
print(reverse_num(number))
