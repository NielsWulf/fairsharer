import ruff

def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration, the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
    values: 1D array of values (list or numpy array)
    num_iterations: Integer to set the number of iterations
    share: Fraction of the highest value to share with neighbors (default is 0.1)  
    """

   
    for _ in range(num_iterations):
   
        max_index = values.index(max(values))

  
        share_value = values[max_index] * share

 
        left_index = (max_index - 1) % len(values)
        values[left_index] += share_value

        right_index = (max_index + 1) % len(values)
        values[right_index] += share_value

        values[max_index] -= 2 * share_value

    return values


result1 = fair_sharer([0, 1000, 800, 0], 1)
result2 = fair_sharer([0, 1000, 800, 0], 2)

print(result1)  
print(result2)  