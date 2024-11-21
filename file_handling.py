#..............................................1


let_file_open1=open('Read.txt','rt')
print(let_file_open1.read())

let_file_open1=open('Read.txt','a')
let_file_open1.write('....Because it mantaine your balance and make your work\n easier and faster!')
let_file_open1.close()

let_file_open1=open('Read.txt','rt')
print(let_file_open1.read())



#...........................................................2


let_open_file2=open('Python.txt','rt')
print(let_open_file2.read())

let_open_file2=open('Python.txt','a')
let_open_file2.write('...Python is so simplest, understandable, easiest and readable language!\n You should be learn python as your first programming language!')
let_open_file2.close()

let_open_file2=open('Python.txt','rt')
print(let_open_file2.read())


#.............................................................3



let_open_file3=open('helloworld.txt','rt')
print(let_open_file3.read())
try:
  let_open_file3=open('helloworld.txt','a')
  let_open_file3.write('Hello world basically is unique syntax that is used in every programming language! hahahaha!')
  let_open_file3.close()
except:
  print('Recreate it!')

let_open_file3=open('helloworld.txt','rt')
print(let_open_file3.read())



#........................................................4


let_file_open4=open('Samaharzen.txt','rt')
print(let_file_open4.read())

let_file_open4=open('Samaharzen.txt','w')
let_file_open4.write('Hi! Im Samahar Sajjad Ahmed Bhatti!..\n Im Python developer, Javascript dveloper and Web developer also!')
let_file_open4.close()

let_file_open4=open('Samaharzen.txt','rt')
print(let_file_open4.read())


#........................................................5

try:
  let_file_open=open('oops.txt','x')
  let_file_open.write('OOps(oriented programming language) consist of multiple properties/attributes and functions/methods.\n It consist of classes  and objects and multiple objects\n can be consist of just one class!\n There are four pillars\n 1) Encapsulation\n 2) Polymorphism\n 3) Abstract\n 4)Inheritance')
  let_file_open.close()

  let_file_open=open('oops.txt','rt')
  print(let_file_open.read())
except FileExistsError:
  print('File Exist!')


#..................................................................6

try:
   let_file_open5=open('Lists.txt','x')
   let_file_open5.write('Lists consist of multiples data but without keys and values!')
   let_file_open5.close()


   let_file_open5=open('Lists.txt','rt')
   print(let_file_open5.readlines())
except FileExistsError:
  print('File exist!')




#.......................................................7


let_file_open6=open('Dictionaries.txt','x')
let_file_open6.write('Dictionaries consist of multiple data but dictionaries have keys and values!')
let_file_open6.close()

let_file_open6=open('Dictionaries.txt','rt')
print(let_file_open6.read())



#..........Finished!..........#