def reverse_string(string_a):
    if len(string_a) > 0:
        return str(reverse_string(string_a[1:])) + string_a[0]
    else:
        return ""
string_a = "sruthi"
reversed_string = reverse_string(string_a)
print(reversed_string)
