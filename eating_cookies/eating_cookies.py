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


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
