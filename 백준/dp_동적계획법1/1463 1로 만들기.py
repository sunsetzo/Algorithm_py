n = int(input())
dp = [0] * (n+1)
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//2], dp[i//3], dp[i-1])+1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        elif i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1
    print(dp[-1])