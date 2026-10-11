class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        adj = defaultdict(set)
        visited = set()

        def adjWord(word, other):
            diff = 0
            for i in range(len(word)):
                if word[i] != other[i]:
                    diff += 1
                if diff > 1:
                    return False

            return True

        def constructGraph(word):
            if word in visited:
                return

            visited.add(word)

            for other in wordList + [beginWord]:
                if word != other and adjWord(word, other):
                    adj[word].add(other)
                    constructGraph(other)

        constructGraph(beginWord)

        q = deque()
        q.append(beginWord)
        seqLen = 1
        visited = set()

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word in visited: continue
                if word == endWord: return seqLen
                visited.add(word)
                for other in adj[word]:
                    q.append(other)

            seqLen += 1

        return 0