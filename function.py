# learn module makes it easier to separate code into multiple files
# and reuse them,
# import module
# module.function()

def say_gello(name): 
    return f'Hello, {name}'

def total(*args):
    result = 0
    for i in args:
        result += i
    return result


