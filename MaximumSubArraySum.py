'''
This is based on Kadane's Algorithm

Link:https://leetcode.com/problems/maximum-subarray/

Time Complexity - O(n)
'''

def maxsubarraysum(arr:list):
    maximum=maxarray=arr[0]
    for i in arr:
        maxarray=max(i+maxarray,i)
        maximum=max(maximum,maxarray)
    print("The Sum of SubArray:",maximum)


arr=[-2,-1,-3,4,-1,2,1,-5,4]
maxsubarraysum(arr)