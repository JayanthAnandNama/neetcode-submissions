class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        var = set(nums)
        longest = 0

        for i in var:
            if (i - 1) not in var:
                length = 1
                while (i + length) in var:
                    length += 1
                longest = max(length, longest)
        return longest
        