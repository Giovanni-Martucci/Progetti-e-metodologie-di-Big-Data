# import sys because we need to read and write data to STDIN and STDOUT
import sys
import math
for y in sys.stdin:
    # to remove leading and trailing whitespace
    y = y.strip()
    key_y, S_value_x, S_value_y = y.split("\t")
    
    p_file = open("P.txt", 'r')
    
    for x in p_file:
        x = x.strip()
        key_x, P_value_x, P_value_y = x.split("\t")
        distance = math.sqrt( (int(P_value_x) - int(S_value_x))**2 + (int(P_value_y) - int(S_value_y))**2 ) 

        print("{}\t{}".format(key_y, [key_x, distance]))
    
    p_file.close()
