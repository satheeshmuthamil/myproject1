def fact(x):
    if x>0:
        f=x+fact(x-1)
    elif x==0:
        f=0
    return f

print(fact(5))