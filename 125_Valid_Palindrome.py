#Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
