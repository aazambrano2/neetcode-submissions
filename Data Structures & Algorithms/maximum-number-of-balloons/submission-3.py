class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        balloon = Counter("balloon")

        res = len(text) #or float("inf")

        for c in balloon:
            res = min(res, count_text[c] // balloon[c])
        return res


        