def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b and b>=c:
        return b
    elif a>=c and a<=b:
        return a
    else: 
        return c
print(main(3,7,1))

