#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if n == 0:      # setting the base case here
        return 1
    if n == 1:      # base cise of factorial i.e. if there is only one number of cookie, we get 1.
        return 1
    elif n < 1:     # negative number of cookies
        return 0
    elif n > 1:           # finally, how can he eat the cookies?
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) #+ eating_cookies(n-4)
        # we apply the factorial function here. where n! = n * (n-1)!
# the factorial function refers to all the different ways of eating cookies, but we have to determine
# if the cookie monster ate 2 cookies first and THEN 2, we add that to the count of one of the ways
# that is why, we do n-1 i.e. eating the cookie one at a time
# then we do, n-2 ie. eating the cookies as 2 first and then 1.
# then eating the cookie 2 first and then 1
# then, eating the cookie all at once. i.e. 3-3 = 0 = 1
# then we do n-3 i.e eating 2 cookies first and then the last one.

def eating_cookies(n, cache=None):

    if n==0:        # number of cookies is 0, return 1
        return 1
    if n < 0:       # number of cookies less than 0
        return 0
    elif cache and cache[n] > 0: # if cach has variables or numbers in it, return that
        return cache[n]
    else:
        if cache is None: # if it is none, we instantiate it at empty and then add the cache[n]
            cache = {}
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache=cache) + eating_cookies(n-3, cache=cache)
        return cache[n] # return cach[n] from adding the new ones
    return cache[n] # return the resulting


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
