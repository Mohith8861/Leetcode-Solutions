// https://leetcode.com/problems/online-stock-span

class StockSpanner:

  def __init__(self):
    self.A = []
    self.Q = 0

  def next(self, price: int) -> int:
    x = 0
    if not self.A :
      self.A.append((price, int(self.Q)))
      self.Q += 1
      return 1
    while self.A and self.A[-1][0] <= price:
      x = self.A.pop()[1]
    w = 0
    if self.A:
        w = self.Q - self.A[-1][1]         
    else:
        w = self.Q +1

    
    self.A.append((price, int(self.Q)))
    self.Q += 1
    return w 
        
   
   


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)