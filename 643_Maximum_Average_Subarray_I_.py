#Sliding Window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sum of the first window of size k
        window_sum = sum(nums[:k])

        # Maximum sum seen so far
        max_sum = window_sum 

        # Slide the window
        for i in range(k, len(nums)):
            # Add the new element
            # Remove the element that leaves the window
            window_sum += nums[i] - nums[i - k]

            # Update maximum sum
            max_sum = max(max_sum, window_sum)

        # Maximum average
        return max_sum / k
