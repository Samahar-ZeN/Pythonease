#.................................................1


try:
  let_take_no1=56
  let_take_no2=0
  print(let_take_no1/let_take_no2)
except ZeroDivisionError:
  print('This statement cant divide by zero(0)')



#...........................................................2

try:
  number_1=90
  number_2=12
  number_3=45
  let_sum=number_1 + number_2 + number_3
  print(let_sum)
except: 
  print('Correct your statement!')



#.......................................4

try:
  let_take_input=int(input('Enter a number:'))
  print(f'Input is:{let_take_input}')
except ValueError:
  print('Enter integer no not string()')



#.....................................................5

try:
  value=12
  value2=17
  if value >= value2 and value<=value2:
         print(True)
  else:
       print(False)
except:
   print('Enter semi colon in if statement!')



#................................6
try:
  n=15
  n2=24
  n3='19'
  print(n + n2/n3)
except:
   print('Enter int in (n3) not str()')




#.................Finished!.............#