import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    x = []
    for i in range(n): 
        x.append(i)
    return x

print(main(5))