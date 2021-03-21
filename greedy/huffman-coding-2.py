f = open('sample-data/huffman.txt', 'r')
data = list(map(int, f.readlines()[1:]))
f.close()

cr = {i: data[i] for i in range(1000)}
meta = [[i] for i in range(1000)]
newid = 1000


while len(cr) > 2:
    k1 = min(cr, key=cr.get)
    w1 = cr.pop(k1)
    k2 = min(cr, key=cr.get)
    w2 = cr.pop(k2)
    
    cr[newid] = w1+w2
    newid += 1
    meta += [meta[k1]+meta[k2]]

byte = [0]*1000

for i in meta:
    for j in i:
        byte[j] += 1
print(max(byte), min(byte))