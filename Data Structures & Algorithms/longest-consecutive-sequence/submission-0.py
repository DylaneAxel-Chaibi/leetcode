class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        L = 0
        starts = []
        for num in nums :
            if num - 1 not in nums :
                starts.append(num)
        for start in starts :
            i = 1
            while start + i in nums :
                i += 1
            if i > L : 
                L = i
        return L