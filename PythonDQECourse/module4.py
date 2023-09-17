# #Functions

def first_function():
    a = 1 + 2
    return a, a+3, a+9

# calling function
a = first_function()
# print(a)


# arguments
def argument_function(a,b,c):
    sum = a + b + c
    return sum

result = argument_function(1,2,3)
# print(result)

# conditional arguments
def conditional_arguments(a = 22, b = 33, c = 44):
    sum = a + b + c
    return sum                    # return sum

resul = conditional_arguments(c =0)   # calling the function If we are mentioning values here it will skip arugments above
# print(resul)                      # printing the result

# arbitrary arguments

def arbitrary_fucntion(*args):
    print(args)
    print(type(args))
    return sum(args)
sum = arbitrary_fucntion(1,2,3,4,5,6,8)
print(sum)

# keyword arguments
def keyword_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(value)

keyword_function(a = 10, b = 12, c = 45)

# recursion
def recursion_fucntion(i):
    if i > 0:
        result = i + recursion_fucntion(i-1)
        # print(f'({i}) + previous+sum = {result}')
    else:
        result = 0
    return result
re = recursion_fucntion(5)
# print(re)

# Scope of varibale
x = 10
def scop():
    global x
    x = 4
    print(x)
scop()
# print(x)

#lambda
a = lambda x: x + 1
print(a(5))
