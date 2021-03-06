import numpy as np

# S: 2 complement
# https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
#
# https://en.wikipedia.org/wiki/Two%27s_complement
#
# TODO
def twos_complement (input_value, num_bits):
    mask = 2**(num_bits - 1)
    return -(input_value & mask) + (input_value & ~mask)

# TODO
def two_complement_b(e):
  for e in pulseOut:
    if e < 0:
        s = 1
    else:
        s= 0
    a = str(s) + str(bin(abs(e))[2:].zfill(14))
    print a

class TwoCompl:
    def __init__(self, NBITS):
        self.NBITS = NBITS
        pass

    def convertList(self, lst):
        out = []
        for e in lst:
            a = np.binary_repr(e, self.NBITS)
            out.append(a)
        return out

    def toFile(self,lst, filename):
        out = self.convertList(lst)

        fo = open(filename, "w")

        for e in out:
            fo.write(e)
            fo.write("\n")
        fo.close()

    def convertString(self, s):
        lenN = len(s) - 1
        expMax = lenN - 1
        print lenN


        sign = -1
        if s[0] == "0":
            sign = 1
        print sign
        n = 1
        exp = expMax 
        for e in s[1:]:
            if e == "0":
                n = 0
            print n,  exp
            exp = exp - 1

def main():
    tw = TwoCompl(16)
    tw.convertString("11111")

if __name__ == "__main__":
        main()
