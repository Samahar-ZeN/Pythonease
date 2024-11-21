#..........................................1
#..........................Task#1........................................


class cats():
    def __init__(self,name,color,legs,ears,eyes,tail):
        self.name=name
        self.color=color
        self.legs=legs
        self.ears=ears
        self.eyes=eyes
        self.tail=tail
    def cats_intro(self):
        print(f'My cat name is:{self.name}')
        print(f'{self.name} has {self.color} color')
        print(f'{self.name} has {self.legs} legs')
        print(f'{self.name} has {self.ears} ears')
        print(f'{self.name} has {self.eyes} eyes')
        print(f'{self.name} has {self.tail} tail')
    def run(self):
        print(f'{self.name} runs')
    def eat(self):
        print(f'{self.name} eat mouse')
    def walk(self):
        print(f'{self.name} walks')
    def chased(self):
        print(f'{self.name} chased the mouse')

selin=cats('Selin','White',4,2,2,1)
selin.cats_intro()
selin.chased()
print(selin.color)


Alexa=cats('Alexa','Black',4,2,2,1)
Alexa.cats_intro()
Alexa.walk()
print(Alexa.color)


#............................................2
#.............................Task#2......................................................


class cars():
    def __init__(self,name,color,seats,mirror,doors,windows,engine_capacity):
        self.name=name
        self.color=color
        self.seats=seats
        self.mirror=mirror
        self.doors=doors
        self.windows=windows
        self.engine_capacity=engine_capacity
    def cars_info(self):
        print(f'My car name is:{self.name}')
        print(f'{self.name} has {self.color} color')
        print(f'{self.name} has{self.seats} seats')
        print(f'{self.name} has {self.doors} doors')
        print(f'{self.name} has {self.windows} windows')
        print(f'{self.name} has {self.mirror} mirror')
        print(f'{self.name} has {self.engine_capacity} capacity')
    def start(self):
        print(f'{self.name} start through automation')
    def brk(self):
        print(f'{self.name} apply break after seeing red signals')
    def restart(self):
        print(f'{self.name} restart after seeing green signals')


MG=cars('MG','Blue',4,5,4,4,1800)
MG.cars_info()
MG.start()

landgruser=cars('Landgruser','Black',4,5,4,4,1600)
landgruser.cars_info()
landgruser.brk()
print(landgruser.color)



#................................................3
#...............................Task#3.....................................


class students_data_information():
    def __init__(self,name,fathername,id,age,course,country,religion):
        self.name=name
        self.fathername=fathername
        self.id=id
        self.age=age
        self.course=course
        self.country=country
        self.religion=religion
    def st_intro(self):
        print(f'My name is:{self.name}')
        print(f'My fathername is:{self.fathername}')
        print(f'My id is:{self.id}')
        print(f'My age is:{self.age}')
        print(f'My course is:{self.course}')
        print(f'My country is:{self.country}')
        print(f'My religion is:{self.religion}')
    def study(self):
        print(f'{self.name} is studying')
    def attend_class(self):
        print(f'{self.name} is attending class')
    def eat(self):
        print(f'{self.name} is eating')


Samahar=students_data_information('Samahar','Sajjad',19908765,20,'Python','Turkiye','Islam')
print(Samahar.course)
Samahar.study()
Samahar.eat()
Samahar.st_intro()

Ozge=students_data_information('Ozge','Torer',123004,25,'Actress','Turkiye','Islam')
Ozge.st_intro()
Ozge.attend_class()
print(Ozge.country)

Hande=students_data_information('Hande','Ercel',13355009,31,'Actress','Turkiye','Islam')
Hande.st_intro()
Hande.study()
print(Hande.course)



#...........................................4
#................................Task#4......................................................


class home():
    def __init__(self,doors,windows,theme,kitchen,garden,rooms,baths,roof):
        self.doors=doors
        self.windows=windows
        self.theme=theme
        self.kitchen=kitchen
        self.garden=garden
        self.rooms=rooms
        self.baths=baths
        self.roof=roof
    def home_structure(self):
        print(f'My home has {self.doors} doors')
        print(f'My home has {self.windows} windows')
        print(f'My home has {self.theme} theme')
        print(f'My home has {self.kitchen} kitchen')
        print(f'My home has {self.garden} garden')
        print(f'My home has {self.rooms} rooms')
        print(f'My home has {self.baths} baths')
        print(f'My home has {self.roof} roof')

    def fans(self):
        print(f'My homes fans run with automation')
    def water(self):
        print(f'My homes water comes through pipes')
    def fount(self):
        print(f'My homes fountain sprinkle water in garden')

samahars_home=home(9,7,'white & black',2,1,10,10,1,)
samahars_home.home_structure()
samahars_home.fount()


Ozges_home=home(10,6,'red & black',2,1,14,12,1,)
Ozges_home.home_structure()
print(Ozges_home.theme)
Ozges_home.fans()




#......................5
#..........................Task#5....................

class my_website():
    def __init__(self,name):
        self.name=name
    header='My name & logo & navbar & login,signin buttons'
    sidebar='dashboard & likes & analytics & reviews'
    sec_1='articles'
    sec_2='Articles images'
    sec_3='Again other Articles'
    sec_4='Again articles images'
    footer='Again logo & social icons and features etc....!!'
    def click(self):
        print(f'When click on the buttons other pages open...!')
    def my_name(self):
        print(f'{self.name}',__name__)
    def icons(self):
        print(f'When click on social icon the sites will be opened....!')


wordflow_website=my_website('Samahar')
wordflow_website.my_name()
print(wordflow_website.footer)
print(wordflow_website.header)
wordflow_website.icons()


website=my_website('Ozge')
website.my_name()
print(website.sidebar)
website.click()


#............................6
#...................Task#6..........................


class dog(cats):
    def voice(self):
        print(f'{self.name} voice is bhaou! bhaou!')
    def speed(self):
        print(f'{self.name} speed is so fast!')


Tesla=dog('Tesla','Black',4,2,2,1)
Tesla.cats_intro()
Tesla.speed()



#................................7
#............................Task#7..............................


class students():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def students_intro(self):
        print(f'My name is:{self.name}')
        print(f'My age is:{self.age}')
    def study(self):
        print(f'{self.name} is studying')
    def attend(self):
        print(f'{self.name} is not attend class')


Samahar=students('Samahar',20)
Samahar.students_intro()
Samahar.study()


Ozge=students('Ozge',31)
Ozge.students_intro()
Ozge.attend()



#..........................8
#...............................Task#8......................................


class bankAccount():
    def __init__(self,account_number,bankbalance):
        self.account_number=account_number
        self.bankbalance=bankbalance
    def deposit(self):
        get_input=int(input('Enter rupees:'))
        print(f'Your deposit cash is:{get_input} and remaing balance is{get_input-self.bankbalance}')

    def withdraw(self):
        get_input2=int(input('enter rupees:'))
        print(f'Your withdraw cash is:{get_input2} and remaing balance is:{get_input2-self.bankbalance}')
    def check_balance(self):
       get_input3=int(input('Enter a number:'))
       if get_input3>0:
           print(f'Your balance is:{self.bankbalance}')
       else:
           print('Your balance is 0')

customer1=bankAccount(123456098,20000)
customer1.withdraw()
customer1.deposit()
customer1.check_balance()


#...................9
#..................Task#9.......................................................


class vehicles():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def vehicles_info(self):
        print(f'This car has is made from {self.make}')
        print(f'This car has {self.model} model')
        print(f'This car made in {self.year}')
    def speed(self):
        print('This car speed is so fast')

Mg=vehicles('China',13,2023)
Mg.vehicles_info()
Mg.speed()


Audi=vehicles('Uk',12,2022)
Audi.vehicles_info()


class car(vehicles):
    def __init__(self,make,model,year,capacity):
        self.make=make
        self.model=model
        self.year=year
        self.capacity=capacity
    def vehicles_info(self):
        print(f'This car has is made from {self.make}')
        print(f'This car has {self.model} model')
        print(f'This car made in {self.year}')
        print(f'capacity is {self.capacity}')


car1=car('England',14,2022,1500)
car1.vehicles_info()
    
        


#...................................10
#..........................Task#10..............................................


class menu():
    def __init__(self,account_number,balance,ammount):
        self.account_number=account_number
        self.balance=balance
        self.ammount=ammount
    def checking_options(self):
        print('option(1) for deposit')
        print('option(3) for withdraw')
        print('option(4) for check balance')
        take_input=int(input('Enter a no:'))
        if take_input==1:
            print(f'Your deposit cash is:{self.ammount} & remainging balance is:{self.ammount-self.balance}')
        elif take_input==3:
            print(f'Your withdraw cash is:{self.ammount} & remaing balance is:{self.ammount-self.balance}')
        elif take_input==4:
            print('Your balance is:',self.balance)
        else:
            print('Invalid option')
            exit(1)
            return menu


c1=menu(1223456,50000,25000)
c1.checking_options()
c1.checking_options()


c2=menu(1239087643,7000,2500)
c2.checking_options()


#..............finished!!!..............#