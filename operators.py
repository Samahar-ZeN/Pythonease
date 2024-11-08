#........Python Operators....

#.........1
#.....Arithematic operators....

a=25
b=12
c=44
#......'+'
print(a+b+c)

#......'-'
print(a-b-c)

#.....'/'
print(b/c)

#.....'*'
print(a*b*c)

#.....'%'
print(a%b)

#.....'//'
#.....Floor division operators...
#......flooor division operators
#.......Flooor division opeartors...
#.....'//
print(a//b)

#.....'**'
#....power operator.......
print(a**2)
print(b**3)
print(c**2)


#.........Asssignment operators.........

d=15
#....'+'
d+=5
print(d)

#.....'-'
d-=7
print(d)

#....'*'
d*=4
print(d)

#.....'/'
d/=6
print(d)

#......'//'
d//=4
print(d)

#....'%'
d%=5
print(d)

#....'**'
d**=2
print(d)

#..........2


e=12
#.....'+'
e+=6
print(e)

#....'-'
e-=8
print(e)

#.....'*'
e*=2
print(e)

#....'/'
e/=4
print(e)

#....'**'
e**=3
print(e)

#....'//'
e//=3
print(e)

#....'%'
e%=2
print(e)


#.........Comparison Operators....

ab=44
cd=10
ef=9
print(ab>cd>ef)
print(ab==cd>ef)
print(cd<ab>ef)
print(ef<cd<ab)
print(ab>ef<cd)
print(ef>cd>ab)
print(cd<ab>ef)
print(not(ab>cd>ef))
print(not(cd==ef<ab))
print(not(ef<cd<ab))
print(not(ab<ef<cd))


#.......Logical Operators.....
#.......And | or operators....
#......Logical operators....

g=34
h=90
i=12
print(g==h and h==i)
print(g<h and h>i)
print(g>h and i<h)
print(i<h and h>g)
print(h==i and i<g)
print(g<h and i<h)
print(not(g<h and i<h))
print(not(h==g and i<h))
print(not(i>h and g<h))
print(not(h>g and i<g))

#........Or operators....

print(h==g or i<h)
print(g<h or i<h)
print(h>g or g<i)
print(h<i or g<i)
print(g<h or h==i)
print(i<h or g>h)
print(i>h or g>h)
print(h>i or g>i)
print(i<h or g>h)
print(not(g<h or h==i))
print(not(g==h or i==h))
print(not(h>i or i<g))
print(not(i<h or h<g))
print(not(g>h or i<h))
print(not(g>h or i>g))


#.......Bitwise operators....
#......Bitwise operators....
#......bitwise operators....
#.....conversion into bits (0,1)
#.......bitwise operators...........

k=4
l=9
print(k & l)
print(10 & 7)
print(8 & 5)
print(6 & 11)
print(12 & 10)
print(4 & 2)
print(9 & 7 & 6 & 5 & 2)
print(5 & 13)
print(6 | 8)
print(9 | 7 | 8)
print(5 | 2)
print(4 | 9 |12)


#......Special Operators....
#....special operators...
#....special operators...
#....special operators...
#....special operators...
#......is operators...
#.....in operators...
#.......is operators....
#......in operators...........


name='Samahar'
q='Samahar'
r='Samahar'
country='Turkiye'
country2='Pakistan'
batch='Python'
t='Sajjad'
fruits=['Apple','Mangoes','Bananas','Grapes']
brands=['J.','Nike','Gulahmed','Pumma']
print('zara' in brands)
print('Zara' in brands)
print('Zara' not in brands)
print('Gucci' in brands)
print('Gucci' not in brands)
print('Pumma' in brands)
print('J.' in brands)
print('Nike' in brands)
print('Strawberry' not in fruits)
print('Strawberry' in fruits)
print('oranges' in fruits)
print('Bananas' in fruits)
print('Grapes' in fruits)
print('kivi' not in fruits)
print(name is q)
print(name is t)
print(q is r)
print(country is batch)
print(country is country2)
print(fruits is brands)

#.....Finished.....:)