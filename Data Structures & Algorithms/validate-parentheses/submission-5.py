class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matcher = {
            ']':'[',
            '}':'{',
            ')':'('
        }



        for char in s:
            if char in matcher.values():
                stack.append(char)
                continue
            elif char in matcher.keys():
                if len(stack) == 0:
                    return False
                if stack.pop() != matcher[char]:
                    return False
        if len(stack) != 0:
            return False
        return True