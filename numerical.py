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
    
    if fa == 0:
        return fa
    elif fb == 0:
        return fb
    
    for x in range(0,iterations):
        mid = 0.5*(a + b)
        fmid = func(mid)
        if fmid == 0:
            return mid
        elif fa*fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid
            
    return mid
    
    
    """if iterations == 0:
        return mid;
    elif fa*fmid < 0:
        return bisection(func,a,mid,iterations - 1)
    else:
        return bisection(func,mid,b,iterations - 1)"""
        
def newtonRaphson(f,df,x,iterations = 5):
    for i in range(0,iterations):
        x = x - f(x)/df(x)
    return x
    
def augment(mat,coeff):
    if len(mat) == len(coeff):
        res = []
        for i in range(len(mat)):
            res += [(mat[i] + [coeff[i]])]
        return res
    else:
        return []

def gauss_jordan_for(mat,coeff):
    if len(mat[0]) == len(coeff):
        aug = augment(mat,coeff)
        m = len(aug)
        n = len(aug[0])
        for i in range(m):
            leading = aug[i][i]
            for j in range(i,n):
                aug[i][j] = (1.0/leading)*aug[i][j]
            for w in range(m):
                if i != w:
                    leading2 = aug[w][i]
                    for j in range(n):
                        aug[w][j] = -leading2*aug[i][j] + aug[w][j]

        res = []
        for i in range(0,m):
            res.append(aug[i][n - 1])
        return res
    else:
        return []

def gauss_jordan_zip(mat,coeff):
    if len(mat[0]) == len(coeff):
        aug = augment(mat,coeff)
        for i in range(len(mat)):
            aug[i] = list(map(lambda x: x/aug[i][i],aug[i]))
            for w in range(len(mat)):
                if w != i:
                    aug[w] = zipWith(lambda x,y: -aug[w][i]*x + y,aug[i],aug[w])
        res = []
        for i in range(len(aug)):
            res.append(aug[i][len(aug[0]) - 1])
        return res
    else:
        return []
