def knapsack(weights, values, weight_limit):
    n = len(weights)
    
    # Create a table to store the maximum value for subproblem
    dp = [[0] * (weight_limit + 1) for _ in range(n + 1)]
    
    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for w in range(weight_limit + 1):
        
            if weights[i - 1] <= w:
                # Choose the maximum of including or excluding the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # If the current item's weight is greater than the current weight limit, exclude it
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right cell of the table contains the maximum value achievable
    return dp[n][weight_limit]

# Example 
weights = [3, 1, 4]
values = [4, 5, 7]
weight_limit = 5

result = knapsack(weights, values, weight_limit)
print("The maximum value achievable is:", result)


