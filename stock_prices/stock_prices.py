#!/usr/bin/python

import argparse
# First, iterate through the list to find the maximum price
# then, find the difference between that price and the minimum prices from all the prices
# before it and then, find the highest profit

def find_max_profit(prices):

    max_prof = [] # make a new array to save the profits in

    for maximum in range(len(prices)):
        for minimum in range(len(prices) - 1):
            if maximum > minimum:
                max_prof.append(prices[maximum] - prices[minimum])
    max_profit = max(max_prof)

    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
