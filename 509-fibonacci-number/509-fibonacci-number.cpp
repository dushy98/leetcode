class Solution {
public:
    int fib(int n) {
        // bottom-up DP
        if (n <= 1){
            return n;
        }
        int p0 = 0, p1 = 1, current;
        for(int i = 2; i <= n+1; i++){
            current = p0 + p1;
            p1 = p0;
            p0 = current;
        }
        return current;
        
    }
};