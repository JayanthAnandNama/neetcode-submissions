class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap to store the counts of the elements from the array
        # then we will traverse through the array and count the frequency of elements in the array
        # then store in the count hashmap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # then create an empty array to store the [count, number] pairs
        # then we have to add each [count (how many times it appeared
        # in the inital array), number (element from array)] pair, and that is the format 
        # we are storing it as, and we sort them in ascending order 
        # so the smallest will be first so it is example: [1,3] it will be 1 appearances for 3
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        # create an empty result array
        # we need the loop to keep running until we find the k elements so that's the condition
        # then we add the pop the pair from arr then we only take what's at index 1, so
        # the pair is [count, num] and at index 1 is num, so it will take the num, and return the array.
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
