def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    x = []
    for i in range(n):
        x.append(k)

    return x
print(main(5,3))