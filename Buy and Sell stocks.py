'''
Link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Time Complexity - O(n)
Space Complexity - O(1)
'''

def buysell(arr):
    l,r=0,1 #left=buy and right=sell
    maxprofit=0
    while r<len(arr):
        if arr[l]<arr[r]:
            profit=arr[r]-arr[l]
            maxprofit=max(maxprofit,profit)
        else:
            l=r
        r+=1
    return maxprofit

prices = [7,1,5,3,6,4]
output=buysell(prices)
print("The maxprofit is=",output)


