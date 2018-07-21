def logit(f):
    def wrapper(*args, **kwargs):
        print('function {} has the following arguements: {}'.format(f,[args]))
        return f(*args, **kwargs)
    return wrapper

# kwargs, keyword arguement can acces by dictionary, like tolerance = some value


# no need line below, if have @logit
# log_square = logit(square)

@logit
def square(x):
    return x * x

# print(log_square(5))
print(square(5))
