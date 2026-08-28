#Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Left pointer of the window
        left = 0

        # Current sum of the window
        window_sum = 0

        # Start with a very large answer
        min_length = float('inf')

        # Expand the window
        for right in range(len(nums)):

            # Add the new element
            window_sum += nums[right]

            # Shrink the window while sum >= target
            while window_sum >= target:

                # Update minimum length
                min_length = min(min_length, right - left + 1)

                # Remove the leftmost element
                window_sum -= nums[left]

                # Move left pointer
                left += 1

        # If no valid subarray was found, return 0
        if min_length == float('inf'):
            return 0

        return min_length
