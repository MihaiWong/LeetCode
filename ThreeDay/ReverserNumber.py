"""给定一个 32 位有符号整数，将整数中的数字进行反转。"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 0:
        print(str(x)[::-1])  # 获取字符串的反转
        result = int(str(x)[::-1])
    else:
        x = -x
        result = 0 - int(str(x)[::-1])
    if -2147483647 <= result <= 2147483646:
        print(result)
        return result
    else:
        return 0


reverse(1534236469)
