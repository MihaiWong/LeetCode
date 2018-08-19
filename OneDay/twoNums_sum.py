"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    """
    求列表中的两数之和
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        result_index = []
        for i in range(0, length):
            x = nums[i]
            temp_lists = nums[i + 1:]
            result = self.get_sums(x, temp_lists, target)
            if len(result) > 0:
                result_index.append(i)
                nums.remove(x)
                result_index.append(nums.index(result[1]) + 1)
                return result_index
            else:
                continue

    def sums(self, num1, num2, target):
        lists = []
        if num1 + num2 == target:
            lists.append(num1)
            lists.append(num2)
        else:
            pass
        return lists

    def get_sums(self, num, lists, target):
        temp = []
        for i in lists:
            lists = self.sums(num, i, target)
            if len(lists) > 0:
                temp = lists
            else:
                continue
        return temp


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 2, 15]
    target = 4
    result = solution.twoSum(nums, target)
    print(result)
