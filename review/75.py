def first_three(L):
    first = max(L)
    L.remove(first)
    second = max(L)
    L.remove(second)
    third = max(L)
    print(first)
    print(second)
    print(third)
first_three([5,2,9,7,4])
