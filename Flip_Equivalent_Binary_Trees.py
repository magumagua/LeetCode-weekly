class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.judge(root1, root2)

     
    def judge(self, root1, root2):
        if root1 and root2:
            if root1.val == root2.val:
                return (self.judge(root1.left, root2.left) and self.judge(root1.right, root2.right) or self.judge(root1.left, root2.right) and self.judge(root1.right, root2.left))
            return False
        else:
            return not root1 and not root2
            