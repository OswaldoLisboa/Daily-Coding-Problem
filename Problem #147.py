def reverse(lst, i, j):
  if (j < len(lst)):
    l1 = lst[0:i]
    l2 = lst[j:i:-1]
    l3 = lst[i:i+1]
    l4 = lst[j+1:]   
    return l1+l2+l3+l4
  else:
    print("Error")