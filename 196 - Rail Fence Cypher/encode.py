def interleave(a, b):
    if (a == "" or b == ""): return a + b
    return a[0] + b[0] + interleave(a[1:], b[1:])

def encode(height, plain, depth=1, atTop=True):
    # top line of pattern
    print depth
    if atTop:
        top = plain[::(height-1)*2]
    elif depth == height:
        return plain[height-1::(height-1)*2]
    else:
        left = plain[depth-1::height+1]
        right = plain[depth-1+2*(height-depth)::height+1]
        print right
        top = interleave(left, right)
    return top + encode(height, plain, depth+1, False)