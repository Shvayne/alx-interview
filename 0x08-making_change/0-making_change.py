#!/usr/bin/python3
"""This code solves the minimum change problem"""

def makeChange(coins, total):
  """A function to calculate the minimum number of coins required to meet a certain amount of change"""
  if total <= 0:
    return 0
  #Initialize an array for storing the minimum coins needed for each amount up to the total
  dp = [float('inf')] * (total + 1)
  dp[0] = 0 #Base case: 0 coins needed to make $0

  for coin in coins:
    for i in range(coin, total + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)
  
  #If dp[total] is still infinity, it means the total cannot be reached
  return dp[total] if dp[total] != float('inf') else -1