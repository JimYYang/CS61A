def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def square(x):
    return x * x

def inverse(f):

    return lambda y : search(lambda x : f(x) == y)

def fir():
    a = 1
    print(a)
    def sec():
        a = 2
    sec()
    print(a)

def t(a):
    return a

def cascase(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascase(n // 10)
        print(n)

def num_partition(n, m):
    if n == 0:
        return 1 # using no parts, recall dp method, this is right!
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return num_partition(n - m, m) + num_partition(n, m - 1)

def split(n):
    return n // 10, n % 10

def sum_num(n):
    if n < 10:
        return n
    num_but_last, last = split(n)
    return sum_num(num_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    num_but_last, last = split(n)
    return luhn_sum_double(num_but_last) + last

def luhn_sum_double(n):
    num_but_last, last = split(n)
    last = sum_num(2 * last)
    return luhn_sum(num_but_last) + last

def sum_num_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum += last
    return digit_sum

def sum_num_recru(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_num_recru(n, digit_sum + last)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

def all_nums(k):
    def help(k, prefix):
        if k == 0:
            print(prefix)
            return
        help(k - 1, prefix * 10)
        help(k - 1, prefix * 10 + 1)
    help(k, 0)


def lens(prev=lambda x: 0):
    def put(k, v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2) # Don't return 0 directly. Because we need this clause to find previous k-v.
        return get, lens(get)
    return put

def storeroom(helium, fn_even, fn_odd):
    even_find, odd_find = False, False
    evens, odds = None, None
    while helium:
        digit, helium = helium % 10, helium // 10
        if digit & 1:
            if not odd_find:
                odds = digit
                odd_find = True
            else:
                odds = fn_odd(odds, digit)
        else:
            if not even_find:
                evens = digit
                even_find = True
            else:
                evens = fn_even(evens, digit)

    return evens > odds

def sculptural(ruler, k):
    if k == 0 or ruler == 0:
        return 0
    a = ruler % 10 + sculptural(ruler // 10, k - 1) * 10
    b = sculptural(ruler // 10, k)

    return max(a, b)

def f(a, b):
    if a > b:
        return f(a - 3, 2 * b)
    elif a < b:
        return f(b // 2, a)
    else:
        return b

def num_eights(n):
    if n == 0:
        return 0
    return (n % 10 == 8) + num_eights(n // 10)

def help(k):
    direc = 1
    x = 0
    i = 1
    while i <= k:
        x += direc
        if num_eights(i) or i % 8 == 0:
            direc = -direc
        i += 1
    return x

def pq(k):
    def helper(i, state, direc):
        if i == k:
            return state
        if num_eights(i) or i % 8 == 0:
            return helper(i + 1, state - direc, direc * -1)
        else:
            return helper(i + 1, state + direc, direc)
    return helper(1, 1, 1)
