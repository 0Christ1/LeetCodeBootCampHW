class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            
            maxArea = max(maxArea, width * h)
        return maxArea

# Time complexity: O(n)
# We can use two pointers to keep track of the left and right indices.
# We can then calculate the area of the container formed by the two pointers.
# If the height of the left pointer is less than the height of the right pointer,
# then we move the left pointer to the right by 1.
# Otherwise, we move the right pointer to the left by 1.
# We keep track of the maximum area and return it at the end.