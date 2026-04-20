class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        if len(nums1) < len(nums2) :
            for n in nums1 :
                if n in nums2 and n not in intersection:
                    intersection.append(n)
        else :
            for n in nums2 :
                if n in nums1 and n not in intersection:
                    intersection.append(n)
        return intersection