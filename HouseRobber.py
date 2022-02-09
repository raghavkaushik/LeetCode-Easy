'''
Link:https://leetcode.com/problems/house-robber/

Time Complexity- O(n)
'''

def houserobber(arr):
    rob1,rob2=0,0
    for i in arr:
        temp=max(i+rob1,rob2)
        rob1=rob2
        rob2=temp
    print("The max we can rob is=",rob2)

nums = [2,7,9,3,1]
houserobber(nums)