import pandas as pd

#df = pd.read_excel('example')

#loop
a = [1,3,4,6]
for y in a:
    print(y)
    
#loop to series
z = pd.Series(a, index=['a','b','c','d']) 
print(z) 

h = pd.DataFrame(a, index=['day1','day2','day3','day4'])

print(h)
    
i = 0
while i < len(a):
  print(a[i])
  i+=1
  
b = [1.5,4.6,7.8]

for y in b:
    print(y)

vocabulary = {
        'slip out':[
        'escabullirse','sgattaiolare',
        'escapulir'
        ],
    'postage':[
        'franqueo',
        'affrancatura',
        'franquia'
        ],
    'neat idea':[
        'buena idea',
        'bella idea',
        'ótima ideia'
        ],
    'copy out':[
        'copiar',
        'copiare',
        'copiar'
        ],       
}

print(pd.DataFrame(vocabulary))

c = pd.DataFrame(vocabulary)

c.to_excel('vocabulary.xlsx')














    
    
"""   
slip out
postage
neat idea
flair talent
opy out
>>> import pandas
>>> import numpy
>>> for x in dragons:
...     print(x)
...     
slip out
postage
neat idea
flair talent
opy out
>>> import pandas as pd
>>> import numpy as np
>>> y = pd.Series(x)
>>> 
>>> print(y)
0    opy out
dtype: object
>>> y = pd.Series(dragons)
>>> print(y)
0        slip out
1         postage
2       neat idea
3    flair talent
4         opy out
dtype: object
>>> z = np.array(y)
>>> print(z)
['slip out' 'postage' 'neat idea' 'flair talent' 'opy out']
>>> a = pd.Series(z)
>>> 
>>> print(a)
0        slip out
1         postage
2       neat idea
3    flair talent
4         opy out
dtype: object
>>> print(a[3])
flair talent
>>> print(a[4])
opy out
>>> 
>>> 
>>> 
>>> print('-'*30)
------------------------------
>>> print('/'*30)
//////////////////////////////
>>> print('/'*3000)

>>> 
>>> for x in slash:
...     print(x)

>>> slash = [2*10]
>>> for x in slash:
...     print(x)
...     
20
>>> veinte = [2*10]
>>> for x in veinte:
...     print(x)
...     
20
>>> veinte = [[2*10]]
>>> for x in veinte:
...     print(x)
...     
[20]
>>> veinte = [[2*10,30*12]]
>>> for x in veinte:
...     print(x)
...     
[20, 360]
>>> print(np.__version__)
2.1.2
>>> b = np.array(40)
>>> for x in b:
...     print(x)

>>> print(b)
40
>>> veinte = [[2*10,30*12]]
>>> for x in veinte:
...     print(x)
...     
[20, 360]
>>> a = ['','','','']
>>> for x in a:
...     print(x)
...     




>>> a = ['/','?','*','%']
>>> for x in a:
...     print(x)
...     
/
?
*
%
>>> a = ['/','?','*','%']
>>> for x in a:
...     print(x)
...     
/
?
*
%
>>> a = ['1','6','5','4']
>>> 
>>> for x in a:
...     print(x)
...     
1
6
5
4
>>> import pandas as pd
>>> y = pd.Series(a)
>>> print(y)
0    1
1    6
2    5
3    4
"""