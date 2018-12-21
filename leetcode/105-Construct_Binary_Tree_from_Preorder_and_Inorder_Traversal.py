# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and preorder) or (len(inorder) != len(preorder)):
            return None
        root_index = inorder.index(preorder[0])
        root = TreeNode(inorder[root_index])
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index + 1:])

        return root

    def beter(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and preorder):
            return None
        root_index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_index])
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])

        return root

    def best(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Tr
        """
        if not (inorder and preorder):
            return None
        self.root_index = 0
        dic = {val: index for index, val in enumerate(inorder)}
        return self.build(0, len(preorder)-1, preorder, dic)

    def build(self, start, end, preorder, dic):
        if (start > end) or (self.root_index == len(preorder)):
            return None
        root = TreeNode(preorder[self.root_index])
        self.root_index += 1
        root.left = self.build(start, dic[root.val]-1, preorder, dic)
        root.right = self.build(dic[root.val]+1, end, preorder, dic)

        return root


"""
[]
[]

[1, 2]
[1, 2]

[1,2,4,8,9,5,10,11,3,6,12,13,7,14,15]
[8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]

[1,2,4,8,5,3,6,7]
[8,4,2,5,1,6,3,7]

[1, 2, 4, 5, 3, 6, 7, 8]
[4, 2, 5, 1, 6, 3, 7, 8]
"""