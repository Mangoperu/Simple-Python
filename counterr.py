from collections import Counter as cs
c = cs([ 'p' , 'a' , 'd'])
print(c)
c.update(['p' , 'b' , 'd'])
print(c)
print(c.most_common(1))
#will print most common as a tuple
d = []
for item  in c.most_common(1) :
    d.append(item[0])

print(d)
