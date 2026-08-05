#https://word-search-2-edon-hall.netlify.app
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None          # Stores complete word at the end


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # -----------------------------
        # Step 1: Build Trie
        # -----------------------------
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # -----------------------------
        # Step 2: DFS
        # -----------------------------
        def dfs(r, c, node):

            # Outside board
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]

            # Already visited
            if ch == "#":
                return

            # Character not in Trie
            if ch not in node.children:
                return

            node = node.children[ch]

            # Found a word
            if node.word:

                result.append(node.word)

                # Prevent duplicates
                node.word = None

            # Mark visited
            board[r][c] = "#"

            # Explore 4 directions
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Undo (Backtrack)
            board[r][c] = ch

        # -----------------------------
        # Step 3: Start DFS everywhere
        # -----------------------------
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
