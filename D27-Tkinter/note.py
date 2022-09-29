# Unlimited Arguments

def add(*args):
    result = 0
    for n in args:
        result += n
    return result

result = add(1,2,3,4,5)
print(result)