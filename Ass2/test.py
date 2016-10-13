def next_seq(size, start, limit):
    if size == 1:
        t = []
        for i in range(start, limit+1):
            t.append([i])
        return t
    if size == limit:
        t = []
        t.append(range(start, limit+1))
        return t
    else:
        s = []
        for i in range(start, limit+2-size):
            for r in next_seq(size-1, i+1, limit):
                if type(r) == type(list()):
                    t = []
                    t.append(i)
                    s.append(list(set(r) | set(t)))
                else:
                    s.append([i,r])
        return s

def restrict_next_seq(size, start, limit, rest):
    if size == 1:
        t = []
        for i in range(start, limit+1):
            if i == rest:
                continue
            t.append([i])
        return t
    if size == limit:
        t = []
        for i in range(start, limit+1):
            if i == rest:
                continue
            t.append(i)
        return [t]
    else:
        s = []
        for i in range(start, limit+2-size):
            if i == rest:
                continue
            for r in restrict_next_seq(size-1, i+1, limit, rest):
                if type(r) == type(list()):
                    t = []
                    t.append(i)
                    s.append(list(set(r) | set(t)))
                else:
                    s.append([i,r])
        return s

def gen_seq(n):
    # for i in range(1, (2**n)):
    #     print i,
    # print

    for i in range(1, n):
        #print next_seq(i, 1, n), len(next_seq(i, 1, n))
        t = next_seq(i, 1, n)
        for x in t:
            s.append(x)
        #print restrict_next_seq(i, 1, n, 1), len(restrict_next_seq(i, 1, n, 1))

gen_seq(4)