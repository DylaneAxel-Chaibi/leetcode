class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def set_intersection(set1, set2) :
            return [x for x in set1 if x in set2]
        if len(nums1) < len(nums2) :
            return set_intersection(set(nums1), set(nums2))
        else :
            return set_intersection(set(nums2), set(nums1))