from encode import encode
from decode import decode

def railFence(inp):
    try:
        t, height, text = inp.split(" ")
        if t == "enc":
            f = encode
        elif t == "dec":
            f = decode
        else:
            assert False
        return f(int(height), text)
    except:
        return "Input Format Error"

if __name__ == "__main__":
    inputs = """
enc 3 REDDITCOMRDAILYPROGRAMMER
enc 2 LOLOLOLOLOLOLOLOLO
enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
dec 4 TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO
dec 7 3934546187438171450245968893099481332327954266552620198731963475632908289907
dec 6 AAPLGMESAPAMAITHTATLEAEDLOZBEN
"""
    for inp in inputs.splitlines(False):
        if inp: print railFence(inp)