class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies_array = [0] * k

        n = len(cookies)

        def dfs(i, zero_count):
            if n - i < zero_count:
                return float('inf')
            
            elif i == n:
                return max(cookies_array)
        
            answer = float('inf')
            for j in range(k):
                zero_count -= int(cookies_array[j] == 0)
                cookies_array[j] += cookies[i]

                answer = min(answer, dfs(i + 1, zero_count))

                cookies_array[j] -= cookies[i]
                zero_count += int(cookies_array[j] == 0)

            return answer
        
        return dfs(0, k)