class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n 
        center = right = 0
        
        for i in range(1, n - 1):
            if i < right:
                P[i] = min(right - i, P[2 * center - i])

            while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2
        return s[start : start + max_len]