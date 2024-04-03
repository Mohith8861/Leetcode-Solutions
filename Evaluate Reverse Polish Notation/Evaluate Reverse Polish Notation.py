// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []
        for i in tokens:
            if i not in '+-/*':
                S.append(int(i))
            else:
                b = S.pop()
                a = S.pop()
                if i == '+':
                    S.append(a + b)
                elif i == '-':
                    S.append(a - b)
                elif i == '*':
                    S.append(a * b)
                elif i == '/':
                    S.append(int(a / b))
        return S.pop(0)

            