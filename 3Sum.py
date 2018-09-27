class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < 0:
                    start +=1 
                elif s > 0:
                    end -= 1
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1; end -= 1
        return res
