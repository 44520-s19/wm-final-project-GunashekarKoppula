import requests

from bs4 import BeautifulSoup

from collections import Counter

file= requests.get("https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1",headers={'User-Agent':'Mozilla/5.0'})

soup = BeautifulSoup(file.text,'html5lib')

ulval=soup.find_all('td',{'class':'titleColumn'})

TopMoviesList=[]

for val in ulval:
    
    #print(val.find('a').get('title'))
    cast =  val.find('a').get('title')
    castlist = cast.split (", ")
    TopMoviesList.append({'director':castlist[0],'actor1':castlist[1],'actor2':castlist[2]})
   # print('--------------------------------------------------')

actorlist=[]
    
for movie in TopMoviesList:
    actorlist.append(movie['actor1'])
    actorlist.append(movie['actor2'])

top11=Counter(actorlist)    
    
topActorCount=[]    
for a in Counter(actorlist).most_common(11):
    topActorCount.append({'name':a[0],'no_of_movies':a[1]})
    
print(top11)




import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import matplotlib.style as style


style.use('default')
style.use('seaborn-talk')
NUM_VALUES = 11
heights = list(top11.values())
heights.sort(reverse=True)
plt.bar(range(NUM_VALUES), heights[:NUM_VALUES],color='#006747')
plt.title('Most Appearances in top rated movies')
plt.ylabel('# Appearance')
keys = list(top11.keys())
keys.sort(reverse=True, key=lambda x: top11[x])
plt.xticks(range(NUM_VALUES), keys[:NUM_VALUES],rotation=30, horizontalalignment='right')
plt.tight_layout()
plt.show()
plt.savefig('myplot.png')
