func concatenatedBinary(n int) int {
    ans, l, M := 0, 0, 1_000_000_007
    for i := 1; i <= n; i++ {
        if (i & (i - 1) == 0){
            l += 1
        }
        ans = ((ans << l) | i) % M
    }
    return ans
}