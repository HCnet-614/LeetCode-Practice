class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
       //把左括号添加至栈/Add left parenthesis to stack
        for(char ch : s.toCharArray()){
            if (ch == '(' || ch =='{' || ch == '['){
                stack.push(ch);
            }else{
                if(stack.isEmpty()){
                    return false;
                }else{
                    char temp = stack.pop(); //取栈顶元素/Get stack top element 
                   //匹配左、右括号/Match left and right parentheses
                    if(ch == ')'){
                        if (temp != '('){
                            return false;
                        }
                    }else if (ch =='}'){
                        if (temp != '{'){
                            return false;
                        }
                    }else if(ch == ']'){
                        if (temp != '['){
                            return false;
                        }
                    }
                }
            }
        }
        return stack.isEmpty()? true:false;
    }
}
