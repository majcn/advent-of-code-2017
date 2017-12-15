start_gen_a = 883
factor_a    = 16807

start_gen_b = 879
factor_b    = 48271

def gen(start, factor, mod):
    v = start
    while True:
        v = (v * factor) % 2147483647
        if v % mod == 0:
            yield v

a = gen(start_gen_a, factor_a, 1)
b = gen(start_gen_b, factor_b, 1)
print len([1 for i in range(40000000) if (a.next() & 65535) == (b.next() & 65535)])

a = gen(start_gen_a, factor_a, 4)
b = gen(start_gen_b, factor_b, 8)
print len([1 for i in range(5000000) if (a.next() & 65535) == (b.next() & 65535)])
