# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and postorder) or (len(inorder) != len(postorder)):
            return None
        root_index = inorder.index(postorder[-1])
        root = TreeNode(inorder[root_index])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        return root

    def beter(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and postorder):
            return None
        root_index = inorder.index(postorder.pop())
        root = TreeNode(inorder[root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root


"""
[]
[]

[1, 2]
[2, 1]

[8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
[8,9,4,10,11,5,2,12,13,6,14,15,7,3,1]

[8,4,2,5,1,6,3,7]
[8,4,5,2,6,7,3,1]

[4, 2, 5, 1, 6, 3, 7, 8]
[4, 5, 2, 6, 8, 7, 3, 1]
"""