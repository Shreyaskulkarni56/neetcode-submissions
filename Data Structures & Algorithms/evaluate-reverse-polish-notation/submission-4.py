class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr={"+","-","*","/"}
        stack = []
        for token in tokens:
            if token in opr:
                a= stack.pop()
                b= stack.pop()
                if token == "+":
                    res = b + a
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = b * a
                else:
                    if a==0:
                        raise valueError("division by zero")
                    res = int(b/a)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]

