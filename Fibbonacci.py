import copy

# Naive recursive version of fibbonacci numbers - This is exponential time
def naiveFib(index):
    if index < 0:
        raise Exception("The first fibbonacci index is 0.")
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return naiveFib(index-1) + naiveFib(index-2)

# Dynamic Programming version of fibbonacci numbers - Linear time
def dpFib(index):
    if index < 0:
        raise Exception("The first fibbonacci index is 0.")

    table = [None] * max(2,index+1)
    table[0] = 0
    table[1] = 1

    for i in range(2,index+1):
        table[i] = table[i-1] + table[i-2]

    return table[index]


# Memoized version of fibbonacci numbers - linear time
def memFib(index):
    memdict = {}
    memdict[0] = 0
    memdict[1] = 1

    def memFibSub(index):
        if index in memdict:
            return memdict[index]
        else:
            result1 = memFibSub(index-2)
            result2 = memFibSub(index-1)
            memdict[index] = result1 + result2
            return memdict[index]

    if index < 0:
        raise Exception("The first fibbonacci index is 0.")

    return memFibSub(index)



# Test that naiveFib and dpFib match
for i in range(0,20):
    assert naiveFib(i) == dpFib(i)

# Test memFib
for i in range(1,100):
    assert memFib(i) == dpFib(i)


# Create memoized decorator
def memoize(func):
    cache = {}
    def get_cached(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return get_cached

# Test decorating naiveFib
naiveFib = memoize(naiveFib)
for i in range(1,100):
    assert naiveFib(i) == dpFib(i)

# Using @ decorated version
@memoize
def fib(index):
    if index < 0:
        raise Exception("The first fibbonacci index is 0.")
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index-1) + fib(index-2)


# Test @ decorated version
for i in range(1,100):
    assert fib(i) == dpFib(i)



# First attempt at a catamorphism/histomorophism version (I'm still a bit unclear on the difference)
# Bananna paper says: A histomorphism is a memoizing variant of a catamorphism, making all previously-computed values available.
# So I think this is a histomorphism
# Also note: I'm not sure what "cansCase" means. I'm just borrowing name from paper.
def histomorphism(index, baseCases, consCase):
    # Guarentee baseCase is always a list
    if not isinstance(baseCases, list):
        baseCases = [baseCases]

    # Initialize cache
    accumulator = {}
    for i in range(len(baseCases)):
        accumulator[i] = baseCases[i]

    # Setup memoization
    def memoize(func):
        def get_cached(x, func2):
            if x not in accumulator:
                accumulator[x] = func(x, func2)
            return accumulator[x]
        return get_cached


    consCase = memoize(consCase)
    return consCase(index, consCase)


def consFib(index, func):
    return func(index-2, func) + func(index-1, func)

# Test histomorphism version
for i in range(1,20):
    assert histomorphism(i, [0, 1], consFib) == dpFib(i)

