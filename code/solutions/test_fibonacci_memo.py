memo = {0:0, 1:1}
def fibm(n):
    if n not in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

