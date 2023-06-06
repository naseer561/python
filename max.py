def maxfun(a,b):   
    '''This is to return max number, this function only accepts 2 input values'''
    if a>b:                 # 20 > 33 False
        return a
    elif a<b:               #20 < 33
        return b  
    else:
        return "both are equal"

a = 33
a = 20
# print(hello.var_naseer)

print(maxfun(a,a))