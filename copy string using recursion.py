def copy_string(string_a,n):
    if n < len(string_a):
        return  string_a[n] + str(copy_string(string_a,n+1))
    else:
        return ""
    
string_a = "sruthi"
string_b = copy_string(string_a,0)
print(string_b)
