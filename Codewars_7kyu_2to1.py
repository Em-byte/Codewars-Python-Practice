"""
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.
"""


def longest(s1, s2):
    s3 = ""
    for i in s1:
        if i not in s3:
            s3 += i
            
    for i in s2:
        if i not in s3:
            s3 += i
            
    return ''.join((sorted(s3)))
