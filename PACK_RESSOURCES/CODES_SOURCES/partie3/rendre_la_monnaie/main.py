# Rendre la monnaie
# Glouton (greedy) | Brute force

# 121
# 50, 20, 10, 5, 2, 1
# 2 x 50
# 1 x 20
# 1 x 1

# 121
# 50, 20, 10, 5, 2
# 2 x 50
# 1 x 20
# ...

# 2 x 50
# 3 x 5
# 3 x 2

#          1  1  0
# 50, 20, 10, 5, 2

# entrée : e classé du plus grand au plus petit
def cash_back_greedy(s, e):
    r = []
    for a in e:
        n = s//a
        r.append(n)
        s -= n*a

    for i in range(len(e)):
        if r[i] > 0:
            print(e[i], "x", r[i])

    if s > 0:
        print("Reste de :", s)
    else:
        print("Toute la monnaie a été rendue")

    return r


def cash_back_brute_force(s, e):

    results = []
    c = [0]*len(e)
    while(c[0]*e[0] <= s):
        
        '''v = 0
        for i in range(len(e)):
            v += c[i]*e[i]'''
        v = sum([c[i]*e[i] for i in range(len(e))])
        # print(c, "->", v)
        if v == s:
            results.append((c.copy(), sum(c)))
            #print("Result found : ", c)

        c[-1] += 1

        i = len(e)-1
        while(v > s):
            # print("sup")
            c[i] = 0
            c[i-1] += 1
            v = sum([c[i]*e[i] for i in range(len(e))])
            # print("sup", c, "->", v)
            i -= 1
            if i == 0:
                break
    print("END")
    results.sort(key=sort_results)
    for r in results:
        print(r)

def sort_results(e):
    return e[1]



#print(cash_back_greedy(121, [50, 20, 10, 5, 2]))
cash_back_brute_force(121, [50, 5, 2])