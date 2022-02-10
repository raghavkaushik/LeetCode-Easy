'''
Link:
https://leetcode.com/problems/merge-sorted-array/

Time Complexity - O(n)
'''


def mergesorted(arr1,arr2,m,n):
    last=m+n-1
    while m>0 and n>0:
        if arr1[m-1]>arr2[n-1]:
            arr1[last]=arr1[m-1]
            m-=1
        else:
            arr1[last]=arr2[n-1]
            n-=1
        last-=1
    while n>0:
        arr1[last]=arr2[n]
        n-=1
        last-=1
    print("The merged array is=",arr1)




nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mergesorted(nums1,nums2,m,n)
