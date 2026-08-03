class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxProfit = 0
        where = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                grumpy[i] = 1
            else:
                grumpy[i] = 0


        i = 0
        while i < len(customers) - minutes + 1:

            real = 0
            best = 0

            for x in range(i, i + minutes):
                real += customers[x] * grumpy [x] 
                best += customers[x]
            
            dif = best - real
            if dif > maxProfit:
                maxProfit = dif 
                where = i

            i += 1
        
        print(where)
        maxCustomers =0 

        for i in range(len(customers)):
            multipler = grumpy[i]
            if i >= where and i<= where + minutes - 1:
                multipler = 1
            maxCustomers += multipler * customers[i]
        return maxCustomers

