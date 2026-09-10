class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we can open close
        #we cant start with open, and we cant close more than we have opened and more than n and we cant open more than n
        #tree looks like  (
        '''              (  )
                        ( )  ( )
        '''
        res = []
        temp = []

        opened_brackets = 0
        closed_brackets = 0


        def helper():
            nonlocal opened_brackets
            nonlocal closed_brackets

            if closed_brackets > opened_brackets:
                return
            
            if opened_brackets > n:
                return

            if len(temp) == 2 * n:
                res.append("".join(temp[:]))
                return 
            
        
            #add ( or ) 
            
            temp.append("(")
            opened_brackets += 1
                
            helper()
            temp.pop()
            opened_brackets -= 1

            temp.append(")")
            closed_brackets += 1
            helper()
            closed_brackets -= 1
            temp.pop()
        
        helper()
        return res