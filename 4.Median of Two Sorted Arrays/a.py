class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        m = total // 2
        # A 始终是较短的那个数组
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        
        # 对 A 进行 BS
        l, r = 0, len(A) - 1
        while True:
            k = (l + r) // 2
            j = m - 2 - k

            A_left_max = A[k] if k >= 0 else float('-infinity')
            A_right_min = A[k+1] if k+1 < len(A) else float('infinity')
            B_left_max = B[j] if j >= 0 else float('-infinity')
            B_right_min = B[j+1] if j+1 < len(B) else float('infinity')

            if A_left_max <= B_right_min and A_right_min >= B_left_max:
                if total % 2:
                    return float(min(A_right_min, B_right_min))
                return (min(A_right_min, B_right_min) + max(A_left_max, B_left_max)) / 2.0
            elif A_right_min < B_left_max:
                # k 偏小
                l = k + 1
            else:
                # k 偏大
                r = k - 1
        

if __name__ == "__main__":
    nums1 = list(map(int, input().strip()[1: -1].split(',')))
    nums2 = list(map(int, input().strip()[1: -1].split(',')))
    
    so = Solution()
    res = so.findMedianSortedArrays(nums1, nums2)
    
    print(res)