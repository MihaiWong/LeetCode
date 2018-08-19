class Solution:
    # 时间复杂度 N的平方
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[y] == target - nums[x]:
                    return x, y

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if a in nums:
                y = nums.index(a)
                if x != y:
                    return x, y
                else:
                    continue
            else:
                continue

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用len()方法取得nums列表长度
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]], x
            # 否则往字典增加键/值对
            else:
                d[a] = x
            print(d)


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    s = Solution()
    s.twoSum2(nums, target)
