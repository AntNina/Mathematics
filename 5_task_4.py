import numpy as np
import itertools

for p in itertools.product("123", repeat=5):
    print(''.join(p))

for p in itertools.permutations("45", 4):
    print(''.join(str(x) for x in p))

for p in itertools.combinations("6789", 8):
    print(''.join(p))

for p in itertools.product("0987", repeat=2):
    print(''.join(p))
