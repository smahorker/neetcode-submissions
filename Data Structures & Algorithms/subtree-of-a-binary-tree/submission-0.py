class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.SameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def SameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.SameTree(s.left, t.left) and self.SameTree(s.right, t.right)
        return False # one is empty and one is non empty, or mismatched vals