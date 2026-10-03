class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 0 - 5$; 1-10$, 2-20$
        curChange = {
            5: 0,
            10: 0,
            20: 0
        }

        #20 -> 10 + 5; 5, 5 ,5
        #10 -> 5
        #
        for bill in bills:
            curChange[bill] += 1

            change = bill - 5

            if change == 15:
                if curChange[10] >= 1 and curChange[5] >= 1:
                    curChange[10] -= 1
                    curChange[5] -= 1
                elif curChange[5] >= 3:
                    curChange[5] -= 3
                else:
                    return False
            elif change == 5:
                if curChange[5] >= 1:
                    curChange[5] -= 1
                else:
                    return False

        return True           
            
    