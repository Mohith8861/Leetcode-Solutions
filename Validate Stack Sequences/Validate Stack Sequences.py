// https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        for x in pushed:
            st.append(x)
            while(st and st[-1] == popped[0]):
                popped.pop(0)
                st.pop()
        return st == []