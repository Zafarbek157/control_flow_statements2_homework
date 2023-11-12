def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<=b and a<=b:
        return a
    elif b<=c and b<=a:
        return b
    else:
        return c
print(main(-1,-3,-5)) 
    