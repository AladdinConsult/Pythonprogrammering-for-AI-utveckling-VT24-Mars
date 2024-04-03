# for i in range(10):
#     print(i)


# def my_range1(n):
#     i=0
#     values=[]
#     while i < n:
#         values.append(i)
#         i += 1
#     return values

# for i in my_range1(10):
#     print(i)


def my_range2(n):
    i=0
    while i < n:
        yield i
        i += 1

# for i in my_range2(10):
#     print(i)
        
g = my_range2(10)

print(type(g))
print(next(g))
print(next(g))
