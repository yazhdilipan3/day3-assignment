def sub(a,b):
    print(a-b)
def mod_sub(fun):
    def inner(a,b):
        if a < b:
            a, b = b, a
        fun(a,b)
    return inner
c =mod_sub(sub)
sub(2,7)


