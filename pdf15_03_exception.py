def get_nodes(f):
    output = []
    for line in f:
        data = line.strip().split()
        try:
            n1 = int(data[0])
            n2 = int(data[1])
        except ValueError:
            print ('Error in reading row')
            n1 = None
            n2 = None
        # finally:
        #     print ('Error in reading row - 2')
        output.append((n1,n2))
    return output

with open('book1.txt', 'rt') as f:
    nodes = get_nodes(f)

print(nodes)

#book1.txt
# a
# b
# c
# 0 1 
# 0 2 
# 0 3 
# 1 48 
# 1 53