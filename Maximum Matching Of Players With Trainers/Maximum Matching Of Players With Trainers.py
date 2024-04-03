// https://leetcode.com/problems/maximum-matching-of-players-with-trainers

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i,j,R = 0,0,0
        l,k = len(players),len(trainers)
        while(i < l and j < k):
            a,b = players[i],trainers[j]
            if(a <= b):
                R += 1
                i += 1
                j += 1
            else:
                j += 1
        return R