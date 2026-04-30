from collections import Counter as cs
from matplotlib import pyplot as plt
import pandas as pd
c= cs()
data = pd.read_csv('data.csv')
l = data['LanguagesWorkedWith']
for items  in l:
    c.update(items.split(';'))
c= c.most_common(15)
print(c)

language =[]
popularity = []
for i in c:
    language.append(i[0])
    popularity.append(i[1])

plt.barh(language , popularity )#, width= 0.25  )
plt.title('kuch to kia h')
plt.savefig('bar.png')
plt.show()



