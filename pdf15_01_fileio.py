

def get_nodes(f):
    output = []
    for line in f:
        data = line.strip().split()
        output.append((int(data[0]), int(data[1])))
    return output

with open('facebook_combined.txt', 'rt') as f:
    nodes = get_nodes(f)

print(nodes)