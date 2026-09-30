class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #1. store d[nums[i]]= i( value: index)
        #2. store diff= target-nums[i]
        #3. check if d[diff] exists in d. if it does, return [i,d[diff]] 
        # edge case d[diff]!=i (then u are checking if same number exisits in d which it does)

        d={}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i

        print(d)

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d and d[diff]!=i:
                return [i,d[diff]]


    
        return []




          








     