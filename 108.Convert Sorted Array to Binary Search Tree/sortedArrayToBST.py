# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

     def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.left)
#            return "{} -> {}".format(self.val, self.right)

class Solution:
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
if __name__ =='__main__':
    print(Solution().sortedArrayToBST([1,2,3,4,5,6,7,8]))
