#............................1
#...............................Task#1................
#........................Make simple Calculator.............................



def calculator(a,b,c,d):
    print(f'Calculation is:{a*b-c+d}')
calculator(12,5,9,10)


#...........................2
#...............Task#2................
#.........................find factorial of number..........................

from math import*
print('The factorial of 3 is:',factorial(3))



#........................3
#..................task#3.........
#...........find ascii value of character..............................


from string import*
print('The ascii value of S is:',ord('S'))



#...................4
#......................Task#4.....................
#...........find factors of numbers.............................................



def factors_of_numbers(number):
    for i in range(1,number+1):
        if number % i==0:
            print(i)
factors_of_numbers(36)




#......................5
#............task#5................
#.............find divisible numbers by another number.................................


def divisible_numbers(list,value):
    for i in list:
        if i % value==0:
            print(i)
divisible_numbers([10,14,19,24,27,38,45,52,54,60,65],12)


#......................6
#................task#6..............
#..................Convert decimal into binary,octal and hexadecimal.....................................



print('The decimal value of 17 into binary is:',bin(17))
print('The decimal value of 17 into octal is:',oct(17))
print('The decimal value of 17 into hexa is:',hex(17))



#...........................7
#....................Task37.............
#...............Display Calendar............................................................


import calendar
year=2024
month=11
print(calendar.month(year,month))


#..........................................8
#.......................task#8.....................
#................main function...................................


let_take_my_name='Samahar Rajput'
print(let_take_my_name,__name__)

#.................Finshed!............#