class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check if the length is the same, if it isn't no point in the program going further
        if (len(s) != len(t)):
            return False
        # then check if sorted of s is equal to sorted of t
        return sorted(s) == sorted(t)
        