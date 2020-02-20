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

# another way to implement this:

def max_profit(prices):
    minimum = prices[0]                # set it at cursor 0
    max_profit = prices[1] - minimum   # find the maximum profit by subtraction
    for i in range(0, len(prices)):    # set up the range for the loop
        for j in range(i + 1, len(prices)):         # nested loop, one step ahead of prices[i]
            if prices[j] - prices[i] > max_profit:  # if the difference between the prices is greater than max_prof
                max_profit = prices[j] - prices[i]  # we set the max profit at the difference.

    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
