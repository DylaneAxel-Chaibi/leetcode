class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        n1 = n2 = 0
        while n1 < m and n2 < n :
            if nums1[n1] <= nums2[n2] :
                res.append(nums1[n1])
                n1 += 1
            else :
                res.append(nums2[n2]) 
                n2 += 1
        if n1 == m :
            res += nums2[n2 : n]
        else :
            res += nums1[n1 : m]
        nums1[:] = res
        