"""
create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""


def filter_list(l):
    lst = []
    for i in list(l):
        if i == str(i):
            l.pop()
        else:
            lst.append(i)
    return lst
