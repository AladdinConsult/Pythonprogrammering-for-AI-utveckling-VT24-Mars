lambda x: x * x

# def func(x):
#     return x*x

# values = [1,2,3,4,5]

# svar = map(lambda x: x + 1, values )
# print(list(svar))

def mapper(helper_func, iterable): 
    result = []
    for value in iterable:
        helper_result = helper_func(value)
        result.append(helper_result)
    return result

values = [1,2,3,4,5]
result = mapper(lambda x:x-1, values)

print(list(result))
