from collections import Counter
class Solution(object):
    def minCost(self, basket1, basket2):
        cnt=Counter(basket1)
        for x in basket2:
            cnt[x]-=1
        arr=[]
        for v,d in cnt.items():
            if d%2!=0:
                return -1
            arr+=[v]*(abs(d)//2)
        arr.sort()
        mn=min(min(basket1),min(basket2))

        total=0
        for i in range(len(arr)//2):
            total+=min(arr[i],2*mn)
        
        return total

        

        