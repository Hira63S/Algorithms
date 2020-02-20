#!/usr/bin/python

import argparse
# First, iterate through the list to find the maximum price
# then, find the difference between that price and the minimum prices from all the prices
# before it and then, find the highest profit

def find_max_profit(prices):

    max_prof = [] # make a new array to save the profits in

    for maximum in range(len(prices)):              # the for loop triggered at first
        for minimum in range(len(prices) - 1):      # then, we find the minimum
            if maximum > minimum:                   # whenever max is greater than the mnimum, we append the profit
                max_prof.append(prices[maximum] - prices[minimum]) # append the profit and then it returns to outer loop
    max_profit = max(max_prof) #find the max profit and we get a result

    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
