def sum_of_multiples_below_1000(x, y):
    """
    Given multiples of x or y below 1000, return the sum. 
    
    Parameters: 
        x: integer
        y: integer

    Example: 
    sum_of_multiples_below_1000(3, 5)
    => 233168 
    """
    
    multiple_sum = 0

    for i in range(1,1000):
        # 'Or' is a short-circuit operator, so common multiples aren't captured
        if i % x == 0 or i % y == 0:
            multiple_sum += i
        
    return multiple_sum



print sum_of_multiples_below_1000(3, 5)
