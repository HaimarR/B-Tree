class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            
            if self.checkSum(nums, index, target):
                num1 = nums.index(self.num1)
                num2 = nums.index(self.num2)
                
                my_list = [num1, num2]
                
                return my_list
    
    def checkSum(self, nums, start_index, target):
        
        self.num1 = nums[start_index]
        check_index = start_index + 1
        
        while check_index < len(nums):
            self.num2 = nums[check_index]
            
            if self.num1 + self.num2 == target:
                return True
            
            check_index += 1
            
        return None
        
    def main(self):
        print(self.twoSum([2,7,11,15,25,40,72,12,44], 50))

if __name__ == "__main__":
    Solution().main()