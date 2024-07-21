s = "0P"


def palindrome(s):
    s = "".join([x.lower() for x in s if x.isalpha() or x.isalnum() ])
    n = len(s)
    l, r = 0, n-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r += -1
    return True

print(palindrome(s))
