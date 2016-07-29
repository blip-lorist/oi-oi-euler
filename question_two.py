
def even_fib_under_four_mil_recursive(x = 0, y = 1, even_sum = 0):
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    Parameters:
        x: default start at 0
        y: default start at 1
        even_sum: collect the sum, starts at 0

    Returns the sum of even-valued numbers under four million
    """

    if y >= 4000000:
        return even_sum 

    next_num = x + y
    if next_num % 2 == 0:
        even_sum += next_num
    
    return even_fib_under_four_mil_recursive(y, next_num, even_sum)



print even_fib_under_four_mil_recursive()
