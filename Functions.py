#........................1
#....................Functions of Python.....
#................functions.........


#.................1


def users():
    print('Hello Python!')
users()

#................2

def hello():
    print('Hello Samahar!')
hello()

#...........3

def hi():
    print('Hello World!!!')
hi()


#.......................4


def my_data(name,Fathername,id,batch,Age,Country,Religion):
    print(f'My name is:{name}')
    print(f'My fathername is:{Fathername}')
    print(f'My id is:{id}')
    print(f'My batch is:{batch}')
    print(f'My age is:{Age}')
    print(f'My Country is:{Country}')
    print(f'My religion is:{Religion}')
my_data('Samahar','Sajjad Ahmed',990876,'Python B7',20,'Pakistan','Islam')


#..........5

def sum(x,y,z):
    print(f'Sum is:{x+y+z}')
sum(9,12,10)

#.......6
def sub(x,y,z):
    print(f'Subtraction is:{x-y-z}')
sub(34,2,1)

#..........7

def mult(x,y,z):
    print(f'Multiplication is:{x*y*z}')
mult(2,15,9)

#.........8
def mod(x,y):
    print(f'Modulus is:{x%y}')
mod(90,9)

#........9

def division(x,y):
    print(f'Division is:{x/y}')
division(25,5)

#..........10

def floordivision(x,y):
    print(f'Floordivision is:{x//y}')
floordivision(93,2)

#..........11



def calculator(a,b,c,d):
    print(f'Calculation is:{a+b-c*d}')
calculator(25,5,6,8)


#...........12


def sqr(r):
    return r*r
let_a=sqr(4)
print(f'Square is:{let_a}')


#..............13



def cube(h):
    return h*h*h
let_a=cube(3)
print(f'Cube is:{let_a}')


#..........14


def frthsqr(b):
    return b*b*b*b
let_a=frthsqr(2)
print(f'Frth Square is:{let_a}')


#.....................15


def fifthsqr(D):
    return D*D*D*D*D
let_a=fifthsqr(7)
print(f'Fifthsqr is:{let_a}')



#...............1
#.............Nonkey(withoutkeys) Arguments......
#..............Nonkeys(withoutkeys) Arguments.....
#........We use single parameer and collection of arguments store in that just(one) single parameter...
#......Collections of arguments store in a sinle parameter....
#.........Collections of arguments store in a single parameter...
#......nonkey arguments same asa a list.....
#......nonkey arguments same as a list......
#........we use '*' in nonkey arguments.........


#.................1


def users(*numbers):
    print(f'Sets of Numbers is:{numbers}')
users(12,3.14,56,7,90,10,4,5)


#................2



def sum(*adding):
    sum=0
    for i in adding:
        sum+=i
        print(sum)
sum(12,10,5,6,7,8,34,99)


#............3

def users(*cars):
    for i in cars:
        print(i)
users('Honda','Civic','Audi','Lissan','MG','Mercedes')


#.........4


def My_dataList(*Samahar):
    print(f'My Data List is:{Samahar}')
My_dataList('Samahar','Sajjad','Python',20,'Pakistan','Islam',990876)


#....................5



def fruits(*fruits):
    for i in fruits:
        print(i)
fruits('Mangoes','Grapes','Oranges','Kivi','Strawberry','Pineapple')



#..............1
#.............wthkeyvalues Arguments.......
#............withkeysvalues arguments.....
#............withkeysvalues arguments.....
#.........keysvalues arguments same as a dictionaries/objects....
#......keysvalues arguments same as a dictionary/objects.....
#.........we use '**' in keysvalues arguments(disctionaries/objects)


#.........1

def users(**data):
    print(f'My data set is:{data}')
users(Name='Samahar Sajjad',id=990876,Batch='Python B7',Age=20,Country='Pakistan',Religion='Islam')

#..............2


def hello(**numbers):
    print(f'Numbers of sets are:{numbers}')
hello(Firstno=15,Secondno=56,Thirdno=10,Fourthno=20,Fifthno=77)


#..............3

def hi(**prices):
    print(f'Prices of brands:{prices}')
hi(Gucci=25000,Pumma=20000,Nike=10000,J=30000,Zara=500000)



#..........4


def fruits_prices(**fruits_prices):
    print(f'Prices of Fruits are:{fruits_prices}')
fruits_prices(Apple=100,Bananas=150,Grapes=200,Pinapple=450,mangoes=300)


#........................5


def users(**currencies):
    print(f'Currencies of different countries are:{currencies}')
users(Pakistan="PKR",Turkiye='Lira',America='Dollars',UK='Ponds',Dubai='Dianr')


#...........tuples.......
#..........tuples same as a list but immutable/Unchangeable...
#...................tuples same as a list but immutable/unchangeable....

#..........1

cars_company_names=('Audi','MG','Civic','Mercedes','Lissan','Landgrusers')
for i in cars_company_names:
    print(i)

#cars_company_names[0]="mehran"

#..........2

const_myData_list=('Samahar','Sajjad',990876,'Pthon B7',20,'Pakistan','Islam')
for i in const_myData_list:
    print(i)

#............3

const_myData_values=(12,3.14,5,17,89)
for i in const_myData_values:
    print(i)


#................Sets......
#............Sets......
#.........Sets.......
#.......we can store our collections/multiples of data in sets and using it for our improvements anf future use....
#..........Sets....
#.......Sets....
#........Sets.......


#......................1


my_2022_dataSet={
    'Total Customers reach:980'
    'Total Sales:560'
    'Customers feedback:Poor!'
}
print(my_2022_dataSet)

#...............2

my_2023_dataSet={
    'Total Customers reach:1500'
    'Total Sales:1390'
    'Customers feedback:Average!'
}
print(my_2023_dataSet)

#............3

my_2024_dataSet={
    'Total customers reach:2160'
    'Total Sales:2000'
    'Customers Feedback:Excellent!!'
}
print(my_2024_dataSet)



#..........4

let_take_data_fromUsers_in_a_set=set()
print(let_take_data_fromUsers_in_a_set)

#.......5

empty_set_forUsers_dataEntring=set()
print(empty_set_forUsers_dataEntring)

#..................6


def users(a=55,b=3,c=16,d=10):
    print(f'Sum is:{a+b+c+d}')
users()


#...........Finished!.........#