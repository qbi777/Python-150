class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([beginWord])

        steps = 1

        while queue:

            for _ in range(len(queue)):

                word = queue.popleft()

                if word == endWord:
                    return steps

                word_chars = list(word)

                for i in range(len(word_chars)):

                    original = word_chars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":

                        if c == original:
                            continue

                        word_chars[i] = c

                        next_word = "".join(word_chars)

                        if next_word in word_set:

                            queue.append(next_word)

                            word_set.remove(next_word)

                    word_chars[i] = original

            steps += 1

        return 0
