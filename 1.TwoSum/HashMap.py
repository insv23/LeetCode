class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if (sub in num_dict):
                return [i, num_dict[sub]]
            num_dict[nums[i]] = i

if __name__ == "__main__":
    trimmed_str = input().strip()[1:-1]
    nums = list(map(int, trimmed_str.split(',')))
    target = int(input())

    so = Solution()
    res = so.twoSum(nums, target)

    print(res)