def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Keep dividing n by the smallest divisor
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            # Add the divisor to the operation count (this represents Copy + Paste operations)
            operations += divisor
            # Reduce n by dividing it by the current divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1
    
    return operations

