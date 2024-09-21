class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateset=set()
        for x in nums:
            if x in duplicateset:  
                return True  
            duplicateset.add(x)
        return False
#time complexity O(n)
#space complexity O(n) because we used extra storage i.e the HashSet