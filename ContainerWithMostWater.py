class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        maxarea = 0
        for i in range(len(height)):
            width = abs(end - start)
            if height[start] < height[end]:
                area = width * height[start]
                start += 1
            else:
                area = width * height[end]
                end -= 1
            if area > maxarea:
                maxarea = area
            
            
            
        return maxarea
