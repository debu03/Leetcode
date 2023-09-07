class Solution(object):
    def inorderTraversal(self, root):
        #Inorder-->Left->Root->Right, so it is recursive call 
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []