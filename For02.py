def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    
    x = ''
    for i in range(n):
        if i != n-1:

            x+=str(i)+','
        else:
            x+=str(i)

    return x
print(main(3))