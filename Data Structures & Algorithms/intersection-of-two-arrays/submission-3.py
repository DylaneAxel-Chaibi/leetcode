class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        mp = {}
        for x in nums1 :
            mp[x] = 1
        for x in nums2 :
            if x in mp and mp[x] == 1 :
                res.append(x)
                mp[x] = 0
        return res