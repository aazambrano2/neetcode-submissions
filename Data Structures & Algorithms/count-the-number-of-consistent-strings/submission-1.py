class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = set(allowed)
        ans = len(words)
        for w in words:
            for c in w:
                if c not in consistent:
                    ans -= 1
                    break
        return ans

        