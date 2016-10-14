from sys import argv

if len(argv) == 2:
    FN = str(argv[1])
else:
    FN = str(raw_input("Enter Input File: "))

F = open(FN, 'r')

n_str = F.readline()
NP = int(n_str.strip()) # Number of Players

u_str = F.readline()
u_strs = u_str.split(",")

U_in = [] # Utilities of various coalitions (not parsed)
for x in u_strs:
    U_in.append(int(x))


U = {} # Utilities of various coalitions (parsed)

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

def gen_seq(n):

    s = []
    for i in range(1, n+1):
        # print next_seq(i, 1, n), len(next_seq(i, 1, n))
        t = next_seq(i, 1, n)
        for x in t:
            s.append(x)
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

def restrict_gen_seq(n, rest):
    s = []
    for i in range(1, n):
        # print restrict_next_seq(i, 1, n, rest), len(restrict_next_seq(i, 1, n, rest))
        t = restrict_next_seq(i, 1, n, rest)
        for x in t:
            s.append(x)
    return s

def Factorial(n):
    f = [1]
    for x in range(1, n+1):
        f.append(f[x-1]*x)
    return f

def tokey(l):
    s = ""
    for x in l:
        s += str(x)
    return s

T = gen_seq(NP)
# print T
for i in range(0, (2**NP)-1):
    # print tokey(T[i])
    U[tokey(T[i])] = U_in[i]
# print U

FACT = Factorial(NP)
#print FACT
for i in range(1, NP+1):
    shapley = 0
    #print i
    shapley += (FACT[0]*FACT[NP-1])*(U[tokey([i])])
    for c in restrict_gen_seq(NP, i):
        t = []
        t.append(i)
        #print c, (FACT[len(c)]*FACT[NP-len(c)-1])*(U[tokey(set(c)|set(t))]-U[tokey(c)])
        shapley += (FACT[len(c)]*FACT[NP-len(c)-1])*(U[tokey(set(c)|set(t))]-U[tokey(c)])
    print "Player", i, "-", round(float(shapley)/float(FACT[NP]), 3)
