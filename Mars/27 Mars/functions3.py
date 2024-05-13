# def func(*args):
#     print(args)

# func()
# func(1)
# func(1,2)
# func(1,2,3)
#-------------------------

# def func2(a,b,**kwargs):
#     print(a,b)
#     print(kwargs)

# func2(1,2,c=3,d=4)
#----------------------------

# def func2(a,b,**kwargs):
#     print(a,b, kwargs['c'], kwargs['d'])
    

# func2(1,2,c=3,d=4)
#---------------------------------

# def func2(a,b,**kwargs):
#     print(a,b)
#     if 'c' in kwargs:
#         print(kwargs['c'])
#     if 'd' in kwargs:
#         print(kwargs['d'])
    

# func2(1,2,c=3)
#-------------------------------

def func3(a,b,*args,name='John',**kwargs):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'args = {args}')
    print(f'name = {name}')
    print(f'kwargs = {kwargs}')

func3(1, 2, 3,'Anna', age=34,email='anna@email.com')