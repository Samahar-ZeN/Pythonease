#........1
#.......print....

print('Samahar Sajjad Ahmed')
print('Hello Python!')
print('Hello World!')
print('Hello Java!')


#.......2
#......Print numbers......

print(20+45)
print(20*2)
print(4*7)
print(2*8)
print(25+9+7)
print(4-5-80)
print(33%3)
print(22/2+9*8)


#.........3

#.......Making calculator......

#.....'+'
a=20
b=67
print(a+b)

#.....'-'

c=25
d=12
print(c-d)

#.....'*'

e=3
f=54
print(e*f)

#......'/'

g=60
h=3
print(g/h)

#......'%'

i=23
j=5
print(i%j)


#.......2nd method.....

k=90
l=55
print(k+l)
print(k-l)
print(k*l)
print(k/l)
print(k%l)

#.....3rd method....(by using function:)


def calculator(x,y,z):
    print(x+y*z)
calculator(7,12,10)



#........4
#....use concatation by adding two or more strings not integers just strings.....
#......Concatation is used for adding two or more strings......
#.....Concatation is used for just adding two or more strings....


name='Samahar Rajput'
fathername='Sajjad Ahmed'
batch='Python'
City='Gujranwala'
State='Punjab'
Country='Pakistan'
print('My name is:',name + ' My father name is:',fathername + ' My id is: 1' + ' My batch is:',batch + ' My city is:',City + ' My country is:',Country + ' My state is:',State)

#......2
#.......2nd method...use adding strings/lines........


print('Hello python Class!', end='')
print(' Hi! Im Samahar Sajjad......',end='')
print(' Im a python developer',end='')
print(' And webdeveloper and javascript developer also....',end='')
print(' Thankyou!')



#........5
#.....Outputs Formattings...
#....We can use output formats.........



value1=67
value2=12
value3=90
value4=54
value5=10
print(('First value is:{}' + ' Second value is:{}' + ' Third value is:{}' + 'Fourth value is:{}' + ' Fifth value is:{}').format(value1,value2,value3,value4,value5))


#.........2


print(('My name is:{}' + ' My father name is:{}' + ' My id:{}' + ' My batch is:{}' + ' My country is:{}' + ' My city is:{}' + ' My state is:{}').format('Samahar','Sajjad',1,'Python','Pakistan','Gujranwala','Punjab'))

#..........6

#.....We can use different methods....such as.......

print(name.capitalize())
print(name.upper())
print(fathername.lower())
print(batch.upper())


#.........7

#.....Get input from users....
#......Input method.....
#......getting inputs from users....


get=input('Enter your name:')
print('My name is:',get)
got=input('Enter your father name:')
print('My father name is:',got)
gott=input('Enter your batch:')
print('My batch is:',gott)
gooten=input('Enter your id:')
print('My id is:',gooten)




#....................2


x=input('What is your name?')
print('My name is:',x)
y=input('What is your fathername?')
print('My father name is:',y)
z=input('What is your country?')
print('My country is:',z)
zx=input('What is your batch?')
print('My batch is:',zx)
xy=input('What is your region:')
print('My region is:',xy)
xv=input('What is your city?')
print('My city is:',xv)
nm=input('What is your state?')
print('My state is:',nm)