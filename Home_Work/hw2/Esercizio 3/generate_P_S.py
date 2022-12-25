import os
import random
from matplotlib import pyplot as plt

filename_p = 'P.txt'
filename_s = 'S.txt'

append_write = 'a' 


dim_p = 9  # N
dim_s = 2   # K <-- <=rad(N)

for element in range(dim_p):
    P = open(filename_p,append_write)    
    
    # Gen x, y --> P
    x = random.randint(2, 400)
    y = random.randint(2, 400)

    # Write into file P.txt
    P.write("{}\t{}\t{}\n".format(element, x, y))
    P.close()

    plt.plot(x, y, marker="o", color="red")
    plt.text(x, y, element)
    

for element in range(dim_s):
    S = open(filename_s,append_write)
    
    # Gen x, y --> S
    x = random.randint(2, 200)
    y = random.randint(2, 200)
    
    # Write into file S.txt
    S.write("{}\t{}\t{}\n".format(dim_p + element, x, y))
    S.close()

    plt.plot(x, y, marker="o", color="blue")
    plt.text(x, y, dim_p + element)
    

plt.show()