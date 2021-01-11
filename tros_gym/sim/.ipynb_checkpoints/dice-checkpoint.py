class Dice(object):
    def __init__(seed=None):
        from numpy.random import default_rng
        if seed != None:
            rng = default_rng(seed)
        else:
            rng = default_rng()
    def roll(n,tn):
        import numpy as np
        vs = rng.integers(1,10,size=n,endpoint=True)
        k=1
        ones = np.ones_like(vs)
        while 10*k < tn and np.isin(10*k,vs):
            crits = vs==10*k
            vs[crits] = vs[crits]+rng.integers(1,10,size=np.sum(ones[crits],endpoint=True))
            k += 1
        return vs>=tn