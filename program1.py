class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')' : '(', '}':'{', ']' : '['}

        for char in s :
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack
        pass
# Solution = Solution()
# print(Solution.isValid("()"))    
# print(Solution.isValid("[])"))    








    



  

