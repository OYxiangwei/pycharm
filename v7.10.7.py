def equal(a,b):
    return a == b
def is_palindrome(n):
    s = str(n)
    for i in range(len(s)-1):
        if equal(s[i],s[len(s)-i-1]):
            continue
        else:
            return False
    return True
output = filter(is_palindrome,range(1,1000))
print(list(output))