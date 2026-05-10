class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        biggest = 0
        for i in range(size-1):
            for j in range(i+1, size):
                area = (j-i) * min(height[i], height[j])
                if area > biggest:
                    biggest = area
        return biggest