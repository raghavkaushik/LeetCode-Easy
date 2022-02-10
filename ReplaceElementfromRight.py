'''
Link:https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Time Complexity : O(n)

Logic :
'''

def greatestelement(arr):
    rightmax=-1
    for i in range(len(arr)-1,-1,-1):
        newmax=max(rightmax,arr[i])
        arr[i]=rightmax
        rightmax=newmax
    print("New Array is=",arr)


arr = [17,18,5,4,6,1]
greatestelement(arr)