# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(sqrt(x))


class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x + 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    lo = mid + 1
            else:
                if (mid - 1) ** 2 < x:
                    return mid - 1
                else:
                    hi = mid - 1

# if x > 2, only need check (1, x//2)