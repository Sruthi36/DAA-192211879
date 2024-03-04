n = int(input())
if n<0 or n==0:
    print("Invalid input")
t1 = 0
t2 = 1
print("{} {}".format(t1,t2))
for i in range(n-2):
    t3 = t1+t2
    t1 = t2
    t2 = t3
    print(t3)


def fibonacci(num):
    if num<0:
        print("invalid input")
    elif num==0:
        return 0
    elif num==1 or num==2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input())
for i in range(num):
    print(fibonacci(i))
