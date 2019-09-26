import random

l = [0, 1, 2, 3, 4, 5]
r = random.sample(l, k=2)  #リストからランダムにk個選ぶ
print(r)

import numpy as np
r = np.random.permutation(l)  #リストをランダムで並び替え
print(r)
