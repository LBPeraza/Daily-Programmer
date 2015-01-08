def decode(height, cipher):
    depths = [0] * len(cipher)
    depth = height
    inc = False
    for i in range(len(cipher)):
        depths[i] = depth
        depth += 1 if inc else -1
        if (depth == height): inc = False
        if (depth == 1): inc = True
    lines = sorted(depths, lambda a, b: -cmp(a, b))
    i = 0
    final = ""
    for depth in depths:
        i = lines.index(depth)
        final += cipher[i]
        lines.pop(i)
        cipher = cipher[:i] + cipher[i+1:]
    return final