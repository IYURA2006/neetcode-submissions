class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #pos - right
        #neg - left

        #if two meet smaller explode
        #only collision if first is right and next is left

        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                lastElem = stack[-1]
                if lastElem > 0:
                    #same remove
                    if lastElem == -asteroid:
                        stack.pop()
                        asteroid = 0

                    #in stack smaller
                    elif lastElem < -asteroid:
                        stack.pop()
                    else:
                        asteroid = 0

            if asteroid:
                stack.append(asteroid)

        
        return stack