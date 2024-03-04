def split(A,B):
    if len(A == 1):
        return A*B
    else:
        half = len(A)//2
        split(A[:half],B[:half])
A = 
