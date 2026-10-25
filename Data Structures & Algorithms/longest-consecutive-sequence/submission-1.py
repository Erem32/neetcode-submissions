class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_count = 0
        for num in nums:

            if num-1 in nums_set:
                continue
            
            temp_num = num
            count = 0
            while temp_num in nums_set:
                count+=1
                temp_num +=1
            if count>max_count:
                max_count = count

        

        return max_count