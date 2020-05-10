def naiveFib(index):
    if index < 1:
        raise Exception("The first fibbonacci index is 1.")
    elif index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return naiveFib(index-1) + naiveFib(index-2)


def dpFib(index):
    if index < 1:
        raise Exception("The first fibbonacci index is 1.")

    table = [None] * max(2,index)
    table[0] = 0
    table[1] = 1

    for i in range(2,index):
        table[i] = table[i-1] + table[i-2]

    return table[index-1]


def memFib(index):
    memdict = {}
    memdict[1] = 0
    memdict[2] = 1

    def memFibSub(index):
        if index in memdict:
            return memdict[index]
        else:
            result1 = memFibSub(index-2)
            result2 = memFibSub(index-1)
            memdict[index] = result1 + result2
            return memdict[index]

    if index < 1:
        raise Exception("The first fibbonacci index is 1.")

    return memFibSub(index)



def memoize(func):
    cache = {}
    def get_cached(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return get_cached


# Test that both implementations match
for i in range(1,20):
    assert naiveFib(i) == dpFib(i)

for i in range(1,100):
    assert memFib(i) == dpFib(i)

naiveFib = memoize(naiveFib)
for i in range(1,100):
    assert naiveFib(i) == dpFib(i)


@memoize
def fib(index):
    if index < 1:
        raise Exception("The first fibbonacci index is 1.")
    elif index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)


for i in range(1,100):
    assert fib(i) == dpFib(i)
