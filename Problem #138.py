def minCoins(n):
  coins = [1, 5, 10, 25]
  if n < 5:
    return n
  else:
    for i in range(3,0,-1):
      if n >= coins[i]:
        return n//coins[i]  + minCoins(n%coins[i])
print(minCoins(4))