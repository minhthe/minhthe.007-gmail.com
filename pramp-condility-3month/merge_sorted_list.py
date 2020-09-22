class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m
        for item in  nums2:
            pos = k   
            nums1[pos] = item
            while pos> 0 and  nums1[pos] < nums1[pos-1]:
                nums1[pos], nums1[pos-1] = nums1[pos-1], nums1[pos]
                pos -= 1
            k += 1
        return nums1
   