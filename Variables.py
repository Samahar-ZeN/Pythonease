#...........methods of writing variable's names....

my_name='Samahar Sajjad'
print(my_name)
my_batch='Python B7'
print(my_batch)
myCountry='Pakistan'
print(myCountry)
myReligion='Islam'
print(myReligion)
my_fav_country_is='Turkiye'
print(my_fav_country_is)

#.............Types of variables.....
#.......1
#.......'String'...........

my_intro='''Hi! Im Samahar Rajput!...
Im Python , javascript and web developer!! if you want to ask any question then
contact with me in inbox...Thankyou!!'''
print(my_intro)
my_full_name='Samahar Sajjad'
print(my_full_name)

#.........2
#.......'Integer'......

let_take_no1=12
let_take_no2=98
let_take_no3=10
let_take_no4=25
let_take_no5=56
print(let_take_no1 + let_take_no2 + let_take_no3 + let_take_no4 + let_take_no5)

#..........3
#.........'Float numbers'.....

number1=12.3
number2=10.4
number3=11.1
number4=7.8
number5=4.23
print(number1 - number2 + number3 *  number4 + number5)

#..............4
#............Boolean.....
#......True/False......

is_this_is_true=True
print(f'Yes this is{is_this_is_true}')

is_this_is_false=False
print(f'Yes this is {is_this_is_false}')

is_this_is_none=None
print(f'Yes this is {is_this_is_none}')


#..............5
#............Lists.....

fruits_list=['Apple','Mango','Strawberry','Kivi','Grapes','Oranges','Bananas']
print(fruits_list)

#........6
#.........'Dictionaries'......

numbers_in_words={
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five'
}
print(numbers_in_words)


#.......7
#........tuples same as a list but immutable/unchangeable....

list_of_brands_names=('Gucci','Zara','Nike','J.','GulAhmed','Pumma')
print(list_of_brands_names)
list_of_brands_prices=(25000,30000,12000.15000,25000,50000)
print(list_of_brands_prices)

#........8
#.........sets........

set_of_vowel_words={
    'a','e','i','o','u'
}
print(set_of_vowel_words)
set_of_names={
    'Samahar','Ugur','Burak','Engin','Ozge','hande'
}
print(set_of_names)
set_of_myData={
    'samahar','sajjad',1,'Python'
}
print(set_of_myData)

#............9
#...............characters....
#...............characters.....
#.........characters........

let_take_firstchar='S'
print(let_take_firstchar)
let_take_scndChar='U'
print(let_take_scndChar)
char3='O'
print(char3)
char4='F'
print(char4)
char5='P'
print(char5)

#................10
#.............implicit/automated data type finder.....

value1=67
value2=9.9
value3=12
value4=89
value5=10
let_calculate=value1 + value2 - value3 + value4 + value5
print(let_calculate)
print(type(let_calculate))

#.....2
no1=90
no2=77
no3=12
no4=5
no5=9
let_min=no1 - no2 - no3 - no4 - no5
print(type(let_min))

#..........11
#.......Explicit/manually convert.....


let_take_number1=int('15')
let_take_number2=float('4.5')
let_take_number3=33
let_take_number4=17
let_take_number5=int('82')
let_take_sum=let_take_number1 + let_take_number2 + let_take_number3 + let_take_number4 + let_take_number5
print(type(let_take_sum))

#........2

number_1=23
number_2=int('45')
number_3=14
number_4=int('7')
number_5=int('9')
let_calculation=number_1 + number_2 - number_3 * number_4 + number_5
print(let_calculation)
print(type(let_calculation))

#.......Finished!........#