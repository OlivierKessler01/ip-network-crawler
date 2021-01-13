# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def __init__(self):
        self.build_array = []
        self.balanced_bst = None
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build_balanced_bst(array: list):
            if len(array) < 1: return 0
            
            mid = round(len(array) / 2)
            node = TreeNode(array[mid])
            node.left = build_balanced_bst(array[0:mid:1])
            node.right =  build_balanced_bst(array[mid+1:len(array)-1:1])
             
            
        def populate_array(node: TreeNode):
            if node is None: return 0
            
            populate_array(node.left)
            self.build_array.append(node.val)
            populate_array(node.right)
            
        populate_array(root)
        build_balanced_bst(self.build_array)
        
        return self.balanced_bst


if __name__ == "__main__":
    Treenode
    sol = Solution()
    sol.balanceBST(TreeNode())