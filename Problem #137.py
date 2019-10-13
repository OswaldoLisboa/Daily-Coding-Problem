class BitArray:
  def __init__(self, size):
    self.bitArray = []
    self.size = size
    for i in range(size):
      self.bitArray.append(0)

  def set(self, i, val):
    if val != 0 and val != 1:
      print("Value Error. Input either 0 or 1.")
    elif i >= self.size:
      print("Index Error")
    else:
      self.bitArray[i] = val

  def get(self, i):
    if i >= self.size:
      print("Index Error")
    else:
      print(self.bitArray[i])