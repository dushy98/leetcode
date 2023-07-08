class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        num = len(weights)
        pair_weights = [0] * (num - 1)
        for i in range(num - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()

        answer = 0
        for i in range(k - 1):
            answer += pair_weights[num - 2 - i] - pair_weights[i]
        
        return answer