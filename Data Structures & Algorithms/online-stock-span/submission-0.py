class StockSpanner:

    # (<price, dur)
    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        dur = 1
        while self.stocks and self.stocks[-1][0] <= price:
            p, t = self.stocks.pop()
            dur += t
        
        if dur != 1:
            self.stocks.append((price, dur))
        else:
            self.stocks.append((price, dur))
        
        return dur
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)