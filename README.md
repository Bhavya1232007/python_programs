class Solution:      
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  
        def io(root,ans):
             if root == None :
                return
             io(root.left,ans)
             ans.append(root.val)
             io(root.right,ans) 
        ans=[]
        io(root,ans)
        return ans   
  
