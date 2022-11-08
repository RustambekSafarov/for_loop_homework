def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    x = []
    y = price
    for i in range(10):
        x.append(y)
        y+=price
    return x
print(main(2.25))