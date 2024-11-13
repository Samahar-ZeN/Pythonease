#...................1
#..............controlflow.....
#.........if elif statement.....


#...........1

a=45
if a<=25:
    print(f'{True}')
else:
    print(f'{False}')

#...........2
b=22
if b<=30:
    print(f'{True}')
else:
    print(f'{False}')


#................3

let_take_input=int(input('Enter a number:'))
if let_take_input<=45:
    print(f'{'Yes'}')
else:
    print(f'{'No'}')


#........4

get_input=int(input('enter any no:'))
if get_input>=50:
    print(f'{True}')
else:
    print(f'{False}')


#..........5

my_age=int(input('Enter your age:'))
if my_age<=25:
    print('yes, You are Allow')
else:
    print('Sorry! You are not Allow')


#...........6

get_age2=int(input('Enter Age:'))
if get_age2>=1 and get_age2<=25:
    print(f'{'Allow'}')
elif get_age2==0:
    print(f'{'Definitely, Not Allow'}')
else:
    print(f'{'Sorry!'}')


#..........7

get_again_input=int(input('Enter any no:'))
if get_again_input>0:
    print(f'{'Positive Number!'}')
elif get_again_input<0:
    print(f'{'Negative Number!'}')
elif get_again_input==0:
    print('Number is zero!')
else:
    print(':)')


#........8

take_input=int(input('Enter a number:'))
if take_input%3==0:
    print(f'{take_input} is odd!')
else:
    print(f'{take_input} is even!')


#.........9

take_value=int(input('Enter a value:'))
if take_value%9==0:
    print(f'{take_value} is Multiple of 9')
else:
    print(f'{take_value} is not Multiple of 9')

#...........10

x , y = 70 , 5
sum = x + y
if sum==70 or x==70 or y==70:
    print(f'{True}')
else:
    print(f'{False}')


#.......................1
#.........Looops....
#............First Loop.....
#.......for looops.....
#.......for loops......
#.......for  loops.....
#.......for looops.....
#.......for loops......


#.............1

names_list=['Samahar','Ugur','Burak','Ozge','Hande','EsraBelgic','Ayca','Furkan']
for i in names_list:
    print(i)

#.........2

my_subj_list=['Math','English','Computer','Urdu','Islamiyat','Civics','Education']
for i in my_subj_list:
    print(i)

#.........3

my_fav_dishes_names=['Biryani','MalaiChicken','Roast','BQ','karahi']
for i in my_fav_dishes_names:
    print(i)


#..........4

my_fav_drinksNames_list=['Sting','Pepsi','CocaCola','MintMart','Fanta']
for i in my_fav_drinksNames_list:
    print(i)

#..........5

my_fav_countryNames_list=['Turkiye','Qatar','Egypt','Iraq','Iran','Azerbijan','Palestine']
for i in my_fav_countryNames_list:
    print(i)


#.......6
programming_langNames_list=['Python','JS','Java','PHP','C++','Ruby']
for i in programming_langNames_list:
    print(i)

#.........7

for i in 'Samahar':
    print(i)
    my_name='Samahar Rajput Bhatti'
for i in my_name:
     print(i)
my_fav_country_is='Turkiye'
for i in my_fav_country_is:
    print(i)
my_fav_lang_is='Python'
for i in my_fav_lang_is:
    print(i)
for i in 'Python B7':
    print(i)
my_fav_hobby_is='Travelling'
for i in my_fav_hobby_is:
    print(i)
my_fav_actress_is='Ozge Torer'
for i in my_fav_actress_is:
    print(i)

#.............8
#........Ranges......

take_numbers=[1,2,3,4,5,6,7,8,9,10]
for i in take_numbers:
    print(i)

for i in range(11):
    print(i)

for i in range(101):
    print(i)

for a in range(1,11):
    print(a)

for a in range(200):
    print(a)

for t in range(1,100):
    if t==21:
        break
    print(t)

for r in range(1,1000):
    if r==51:
        break
    print(r)


for b in range(1,3000):
    if b==1001:
        break
    print(b)


for i in range(1,100):
    if i==11:
        break
    print(i)


for e in range(1,11):
    if e==2:
        continue
    elif e==5:
        continue
    elif e==7:
        continue
    elif e==9:
        continue
    print(e)



for i in range(1,50):
    if i>=11 and i<=20:
        continue
    print(i)



for t in range(1,21):
    if t>=1 and t<=10:
        continue
    print(t)



for even in range(2,45,2):
    print(even)



for odd in range(1,50,2):
    print(odd)



for ev in range(2,50,4):
    print(ev)

for od in range(3,60,2):
    print(od)


#.................2
#...........While Loops....

#..........1

x=1
while x<=10:
    print('Samahar Rajput')
    x+=1

#........2

y=1
while y<=5:
    print('Turkiye')
    y+=1


#.........3

a=1
while a<=20:
    print(a)
    a+=1


#..........4

let_tak_value=1
while let_tak_value<=50:
    print(let_tak_value)
    let_tak_value+=1

#......5

c=1
while c<=25:
    print(c)
    c+=1

#.......6
odd=1
while odd<=55:
    print(odd)
    odd+=2


#......7

even=2
while even<=60:
    print(even)
    even+=2

#.......8

x=1
sum=1
while x<=15:
    sum=sum+x
    print(sum)
    x+=1

#.......9

a=1
sum=0
while a<=10:
    sum=sum+a
    print(sum)
    a+=1

#.........10

b=1
sum=1
while b<=5:
    sum+=b
    print(sum)
    b+=1 

#.........Finished:).......#