from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for key in count.values():
            if key % 2 == 1:
                return False
        return True

        