###Testing Alogorithms imported from other files

from Herp.derp.Sort_algo import linear_search   
a=[1,98,76,5,4,6]
n=4
r=linear_search(a,n)

if (r=='False'):
    print('Not Found')
else:
    print('Found')

from Herp.derp.Sort_algo import max_value
x= 300
y=500
z=(max_value(x,y))
print(z)

from Herp.derp.Sort_algo import sort_bubble
b= sort_bubble(a)
print(b)