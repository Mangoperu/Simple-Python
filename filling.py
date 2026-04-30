from matplotlib import pyplot as plt
import pandas as pd


data =pd.read_csv('data (1).csv')
age = data['Age']
all = data['All_Devs']
python = data['Python']
java = data['JavaScript']

plt.plot(age , all  , label = 'all dev' , color= 'g' , linestyle ='--')
plt.plot(age , python , label = 'python' )
plt.plot(age, java , label = 'javascript')



plt.fill_between(age , all , python , alpha = 0.25 , where = (all >=40000) , interpolate=True)



plt.xlable = 'ages'
plt.ylable = 'average dev salary'
plt.title = 'kuch to kia h'


plt.legend()
plt.tight_layout()
plt.savefig('plot(1).png')
plt.show()


