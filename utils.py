import time

def runtime(f,args):
    start = time.perf_counter()
    f(*args)
    end = time.perf_counter()
    return end - start

def avg_runtime(f,args,iters = 100):
    counter = 0
    for i in range(iters):
        counter += runtime(f,args)
    return counter/iters

def zipWith(f,a,b):
    if len(a) == len(b):
        return [f(a,b) for (a,b) in zip(a,b)]
    else:
        return []