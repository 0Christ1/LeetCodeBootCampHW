class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for elem in nums:
            if elem in dic and dic[elem] >= 1:
                return True
            else:
                dic[elem] = dic.get(elem, 0) + 1
        return False

# Time complexity: O(n)
# We can use a dictionary to store the number of times each element appears in the list.
# If the number of times an element appears is greater than or equal to 2, then we return True.
# Otherwise, we return False.