class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count1=0
        count2=0
       
        for i in range(len(bills)):
            if bills[i]==5:
                count1+=1
            elif bills[i]==10 :
                if count1==0:
                    return False
                count2+=1
                count1-=1
            else :
                if count2>0 and count1>0:
                   count1-=1
                   count2-=1
                elif count1 >= 3:
                   count1-=3
                else :
                   return False 
        return True 
