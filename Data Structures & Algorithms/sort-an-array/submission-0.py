class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r) :
            left, right = arr[l:m+1], arr[m+1:r+1]
            l1, l2, res = 0, 0, []
            while l1 < len(left) and l2 < len(right) :
                if left[l1] <= right[l2] :
                    res.append(left[l1])
                    l1 += 1
                else :
                    res.append(right[l2])
                    l2 += 1
            if l1 == len(left) :
                res += right[l2:]
            else :
                res += left[l1:]
            arr[l:r+1] = res

        def mergeSort(arr, l, r) :
            if l >= r :
                return
            m = l + (r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums)-1)
        return nums

