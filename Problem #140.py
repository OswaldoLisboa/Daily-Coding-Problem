def finder(l):
  l0 = []
  i = 0
  while i in range(len(l)) and len(l0) < 2:
    l2 = list(l)
    del l2[i]
    if l[i] not in l2:
      l0.append(l[i])
    i += 1
  return l0

l = [2,4,6,8,10,2,6,10]
print(finder(l))