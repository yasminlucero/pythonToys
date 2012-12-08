## basketball simulation
def G2wins(p):
    try:
        import numpy.random as rand
        rand_loaded = True
    except ImportError:
        rand_loaded = False
    if (p<0 or p>1): print "The input is not a probability"
    elif p==0: print "Strategy irrelevant; always lose both games when p=0"
    elif p==1: print "Strategy irrelevant; always win both games when p=1"
    else:
        iterations = 10000
        tol = 0.01
        G1 = rand.binomial(1, p, size=iterations).sum()
        G2 = rand.binomial(3, p, size=iterations)
        G2 = (G2 >= 2).sum()
        if abs(G1-G2) < (iterations*tol): return 'Tie'
        else: return G2 > G1
    