class Solution(object):
    
    def binary_search(self, nums, target, start, stop, index_result):
        mid = ((stop - start) // 2) + start
        
        if(target == nums[mid]):
            return mid
        
        if target > nums[mid]:
            return self.binary_search(nums, target, mid, stop, index_result)    
        elif target < nums[mid]:
            return self.binary_search(nums, target, start, mid, index_result)
        
        if ((start == mid or stop == mid) and target != nums[mid]):
            return -1
        
        
        return mid
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = self.binary_search(nums, target, 0, len(nums) -1, 0)
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.search([-1,0,3,5,9,12], 2)
    print(result)
        
