'''
Link:https://leetcode.com/problems/two-sum/

Time and Space Complexity: O(n)
'''

def twosums(arr,target):
    prevmap={}
    for i, n in enumerate(arr):
        diff=target-n
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[n]=i

#if arr is sorted
def twosumspart1(arr,target):
    l,r=0,len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target:
            return [l,r]
        if arr[l]+arr[r]>target:
            r-=1
        if arr[l]+arr[r]<target:
            l+=1

nums=[2,7,11,15,21]
target=22
output=twosums(nums,22)
print(output)

