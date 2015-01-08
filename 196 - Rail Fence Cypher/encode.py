def encode(height, plain):
    lines = ["" for _ in range(height)]
    depth = 0
    inc = True
    for c in plain:
        lines[depth] += c
        depth += 1 if inc else -1
        if (depth == height - 1): inc = False
        if (depth == 0): inc = True
    return "".join(lines)