class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate (nums):
            current = target - n
            if current in prevMap:
                return [prevMap[current], i]
            else:
                prevMap[n] = i

        