class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                A = [[num, i] for i, num in enumerate(nums)]
                A.sort()
                i, j = 0, len(nums) - 1
                while True :
                    if A[i][0] + A[j][0] == target : 
                        return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
                    elif A[i][0] + A[j][0] > target :
                        j = j - 1
                    else :
                        i = i + 1
                return []
        