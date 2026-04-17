class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        l, r = 0, len(heights) - 1
        while l < r :
            ca = (r - l) * min(heights[l], heights[r])
            ma = max(ma, ca)
            if heights[l] < heights[r] :
                l += 1
            else :
                r -= 1
        return ma
            