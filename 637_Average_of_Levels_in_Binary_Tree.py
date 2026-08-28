#Breadth First Search (BFS)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:

            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):

                node = queue.popleft()

                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            average = level_sum / level_size

            result.append(average)

        return result
