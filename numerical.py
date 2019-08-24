def incrementalSearch(func,a,b,delta= 0.01,precision= 4):

        x1 = a
        x2 = a + delta
        f1 = func(x1)
        f2 = func(x2)
        
        while f1*f2 > 0:
            if x1 > b:
                return (None,None,'None')

            x1 = x2
            x2 = round(x1 + delta,precision)
            f1 = f2
            f2 = func(x2)

        if f1 == 0:
            return (x1,x2,'left')
        elif f2 == 0:
            return (x1,x2,'right')
        else:
            return (x1,x2,'center')

def bisection(func,a,b,iterations = 20):

    fa = func(a)
    fb = func(b)

    mid = 0.5*(a + b)

    fmid = func(mid)
    if iterations == 0:
        return mid;
    elif fa*fmid < 0:
        return bisection(func,a,mid,iterations - 1)
    else:
        return bisection(func,mid,b,iterations - 1)

