# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        up = n

        #1 2 3 4 5
        # 3

        while low <= up:
            mid = (low + up) // 2
            responce = guess(mid)

            if responce == 0:
                return mid
            elif responce == -1:
                up = mid - 1
            elif responce == 1:
                low = mid + 1

         
