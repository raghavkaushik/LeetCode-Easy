'''
Link:https://leetcode.com/problems/diameter-of-binary-tree/

Time Complexity - O(n)
'''

def diameter(node):
    res=[0]
    def dfs(root):
        if not root:
            return -1
        left=dfs(root.left)
        right=dfs(root.right)
        res[0]=max(res[0],2+left+right)
        return 1+max(left,right)
    dfs(node)
    return res[0]

# OR

def height(node):
    if not node:
        return -1
    else:
        return 1+max(height(node.left,height(node.right)))



def invertbtree(root):
    if not root:
        return None

    tmp=root.left
    root.left=root.right
    root.right=tmp

    invertbtree(root.left)
    invertbtree(root.right)
    return root
