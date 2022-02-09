'''
Link: https://leetcode.com/problems/valid-anagram/

Time Complexity: O(n+m)
Space Complexity: O(s+t) or O(1)
'''
import collections


def anagrams(method,str1,str2):
    if len(str1)!=len(str2):
        return False
    if method=='1':
        if sorted(str1)==sorted(str2):
            return True
    elif method=='2':
        if collections.Counter(str1)==collections.Counter(str2):
            return True
    else:
        count1={}
        count2={}
        for i in range(len(str1)):
            count1[str1[i]]=1+count1.get(str1[i])
            count2[str1[i]] = 1 + count2.get(str1[i])
        for c in count1:
            if count1[c]!=count2.get(c,0):
                return False
        return True
    return False

