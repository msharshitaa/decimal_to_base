def decimal_to_base(A, B):
    if A == 0:
        return "0"
    result = ""
    while A > 0:
        remainder = A % B
        result = str(remainder) + result
        A //= B
    return result
A=int(input())
B=int(input())
print(decimal_to_base(A,B))