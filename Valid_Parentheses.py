#Problem num.20
#If character is '(', '{', or '[', add the complementary closing bracket to the stack. 
#If character is not one of those, pop the stack and compare it to current. 
#If they match continue, if not return false. At end of string if stack is empty then return true
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {'{':'}', '}':'{', '[':']', ']':'[', '(':')', ')':'('}
        for char in s:
            #Push opening brackets
            if char in ['(','{','[']:
                stack.append(char)
            elif char in [')','}',']']:
                if len(stack) == 0:
                    return False
                if stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        
