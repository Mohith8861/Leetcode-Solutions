// https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes))//2
        for i in bobSizes:
            if i + diff in aliceSizes:
                return [i+diff,i]
