"""给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。"""


class Solution:
    """
    从排序数组中删除重复项
    """

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                print(newTail, i)
                newTail += 1
                nums[newTail] = nums[i]
                print(newTail)
                print(nums)
        return newTail + 1


if __name__ == '__main__':
    s = Solution()
    num = [1, 1, 1, 3, 2, 3, 2]
    nums = [1, 1, 3, 1]
    s.removeDuplicates(nums)
