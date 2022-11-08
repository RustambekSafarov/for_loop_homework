def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    sum = 1
    for i in range(N):
        if i != 0:
            sum += 1/i
    return sum
print(main(4))