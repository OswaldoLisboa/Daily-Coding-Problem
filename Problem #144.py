def lrgNumIndex(lst, i):
  j = 1
  after = False
  before = False
  while((i+j < len(lst) or i-j >= 0) and not(before and after)):
    if(i-j >= 0 and lst[i] < lst[i-j]):
      before = True
    elif(i+j < len(lst) and lst[i] < lst[i+j]):
      after = True
    if(before):
      return i-j
    elif(after):
      return i+j
    j += 1
  return None
l = [7, 7, 3, 5, 6, 7]
print(lrgNumIndex(l, 4))