num = int(input("Enter a number"))
sum = 0
temp = num
while temp> 0:
    rem = temp % 10
    sum += rem ** 3
    temp = temp // 10
if sum == num:
    print("Armstrong number")
else:
    print("Not an armstrong number")
