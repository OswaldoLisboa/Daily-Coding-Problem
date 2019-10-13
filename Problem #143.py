def pivot(lst, x):
  bg = []
  eq = []
  sm = []
  for i in range(len(lst)):
    if(lst[i] > x):
      bg.append(lst[i])
    elif(lst[i] < x):
      sm.append(lst[i])
    else:
      eq.append(x)
  return(sm+eq+bg)
lst = [9, 12, 3, 5, 14, 10, 10]
print(pivot(lst, 20))