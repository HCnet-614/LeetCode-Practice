class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if i == '}':
                        if temp!='{':
                            return False
                    elif i == ')':
                        if temp != '(':
                            return False
                    elif i == ']':
                        if temp != '[':
                            return False
        return True if len(stack )== 0 else False
