class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        newarr = []
        nums.sort()
        start = 0
        end = len(nums)-1
        newarr = []
        print(nums)
        while start < end:
            keyvalue = nums[start] + nums[end]
            print("key value " + str(keyvalue))
            print(nums[start+1:end])
            if -keyvalue in nums[start+1:end]:
                print("nums start " + str(nums[start]))
                print("nums -keyvalue " + str(nums.index(-keyvalue)))
                print("nums end " + str(nums[end]))
                if [nums[start],nums[nums.index(-keyvalue)],nums[end]] not in newarr:
                    newarr.append([nums[start],nums[nums.index(-keyvalue)],nums[end]])
                print("new array" + str(newarr))
            if keyvalue < 0:
                start += 1
                print("nums start " + str(nums[start]))
            else:
                end -= 1
                print("nums end " + str(nums[end]))

        return newarr
