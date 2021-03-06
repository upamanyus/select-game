#!/usr/bin/env python3

import random
import numpy as np
from statistics import median

def getrandsubset(n, k):
    return np.random.permutation(range(1, n+1))[:k] # TODO: https://en.wikipedia.org/wiki/Reservoir_sampling

def getrandsubset(n, k):
    return np.random.permutation(range(1, n+1))[:k] # TODO: https://en.wikipedia.org/wiki/Reservoir_sampling

def run_one(n, k, algA, algB):
    """
    Picks two random subsets of size k from {1...n}. Uses algA and algB to
    select a single integer from each, and returns true iff they agreed on the
    integer.
    """
    A = getrandsubset(n, k)
    B = getrandsubset(n, k)
    intA = algA(A)
    intB = algB(B)
    assert(intA in A)
    assert(intB in B)
    # print(A, B, intA, intB)
    return intA == intB

def run_many(n, k, algA, algB, iters):
    s = 0
    t = 0
    for i in range(iters):
        if run_one(n, k, algA, algB):
            s += 1
        t += 1
    print("successes/trials = {0}/{1} ≈ {2}".format(s, t, float(s)/float(t)))
    return float(s)/float(t)

algMax = max
algMin = min
algMedian = median

def main():
    random.seed(0xdeadbeef)
    np.random.seed(0xdeafbeef)
    print("running minimum algorithm on both")
    run_many(10, 3, algMin, algMin, 200000)
    print("running median algorithm on both")
    run_many(10, 3, algMedian, algMedian, 200000)
    print("running min on one, and max on the other")
    run_many(10, 3, algMax, algMin, 200000)

if __name__=='__main__':
    main()
