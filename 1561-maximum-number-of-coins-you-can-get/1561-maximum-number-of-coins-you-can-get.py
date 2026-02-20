class Solution(object):
    def maxCoins(self, piles):
       

        coin=0
        piles.sort()
        
        l= len (piles)
        for i in range(l//3, l,2):
            coin+=piles[i]
        return coin
            

            

                
               