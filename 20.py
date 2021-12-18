class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)   #把左括号添加至栈/Add left parenthesis to stack 
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()  #取栈顶元素/Get stack top element 
                    #匹配左、右括号/Match left and right parentheses
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
