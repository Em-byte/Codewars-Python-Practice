"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    string = string.lower()
    s = []
    count=0
    for i in list(string.lower()):
        if i not in s:
            s.append(i)
            count+=1
        if i in s:
            count+=0
    if count == len(string) or count == 0:
        return True
    else:
        return False
