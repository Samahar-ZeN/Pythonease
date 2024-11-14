#...............1
#.........Data Types.....
#...........dictionaries....
#........Dictionaries/Objects......


#..........1

my_data_lists={
    'Name':'Samahar Sajjad',
    'Father Name':'Sajjad Ahmed Bhatti',
    'Age':20,
    'Course':'Python',
    'Hobbies':['Travelling','Eating','Sleeping','Programming'],
    'Country':'Pakistan',
    'ID':12390
}

print(my_data_lists)
#.......Access Methods.....

print(my_data_lists.get('Name'))
print(my_data_lists.get('ID'))
print(my_data_lists.get('Course'))
print(my_data_lists.get('Hobbies')[3])

print(my_data_lists.values())
print(my_data_lists.keys())

print(my_data_lists.items())
print(my_data_lists.pop('Father Name'))
print(my_data_lists.popitem())

my_data_lists['Country']='Turkiye'
my_data_lists['Course']='Python B7'
my_data_lists['Name']='Samahar Sajjad Ahmed'
print(my_data_lists)

my_data_lists['Religion']='Islam'
print(my_data_lists)
my_data_lists['FavDish']='Biryani'
my_data_lists['favcountry']='Turkiye'
my_data_lists['About']='Hello! Im Python Developer!'
print(my_data_lists)


#....................2


Persons_personal_dataLists=[
    {
        'Name':'Samahar Sajjad Ahmed',
        'Course':'Python',
        'Id':123490,
        'Age':20,
        'favHobbies':['Travelling','Eating','Sleeping','Programming','Walking'],
        'Country':'Pakistan'
    },

    {
        'Name':'Ozge Torer',
        'Course':'IT',
        'Age':25,
        'favHobbies':['Travelling','Eating','Dancing','Acting'],
        'Country':'Turkiye',
        'Id':990011
    },

    {
        'Name':'Burak deniz',
        'Age':36,
        'Id':13450,
        'Course':'Digital Marketing',
        'Country':'Turkiye',
        'favHobbies':['Travelling','Acting','Eating']
    },

    {
        'Name':'Hande Ercel',
        'Id':224400,
        'Age':31,
        'Course':'Web development',
        'favHobbies':['Travelling','Acting','eating','Dancing'],
        'Country':'Turkiye'
    },

    {
        'Name':'Ugur gunes',
        'Id': 345001,
        'Age':34,
        'Course':'IT',
        'favHobbies':['Travelling','Acting','Eating','Sleeping'],
        'Country':'Turkiye'
    }
]

print(Persons_personal_dataLists)

#.........Methods of Dictionaries.......

#........Method#1.....
#.......Get Method.........

print(Persons_personal_dataLists[2].get('Name'))
print(Persons_personal_dataLists[0].get('Name'))
print(Persons_personal_dataLists[0].get('Course'))
print(Persons_personal_dataLists[4].get('favHobbies')[1])
print(Persons_personal_dataLists[4].get('Name'))
print(Persons_personal_dataLists[1].get('Id'))
print(Persons_personal_dataLists[0].get('favHobbies')[3])


#..........Method#2......
#......Get (keys) & (values)......

print(Persons_personal_dataLists[0].values())
print(Persons_personal_dataLists[4].values())
print(Persons_personal_dataLists[3].values())
print(Persons_personal_dataLists[1].values())
print(Persons_personal_dataLists[2].keys())

#..........Method#3....
#.....pop Method......

print(Persons_personal_dataLists[3].pop('Age'))
print(Persons_personal_dataLists[1].pop('favHobbies')[0])

#........Method#4....
#.........PopItem Method.....

print(Persons_personal_dataLists[4].popitem())
print(Persons_personal_dataLists[3].popitem())

#..........Method#5.....
#..........items() Methods....

print(Persons_personal_dataLists[0].items())
print(Persons_personal_dataLists[4].items())


#.........Method#6.....
#......Adding/Updating Methods....

Persons_personal_dataLists[0]['Country']='Turkiye'
Persons_personal_dataLists[1]['Country']='Yemen'
Persons_personal_dataLists[2]['Country']='America'
Persons_personal_dataLists[3]['Country']='Austrailia'
Persons_personal_dataLists[4]['Country']='Iraq'
print(Persons_personal_dataLists)

#...........Addding.......

Persons_personal_dataLists[0]['Religion']='Islam'
Persons_personal_dataLists[1]['Religion']='Islam'
Persons_personal_dataLists[2]['Religion']='Islam'
Persons_personal_dataLists[3]['Religion']='Islam'
Persons_personal_dataLists[4]['Religion']='Islam'
print(Persons_personal_dataLists)

#..........making dictionary new Method.................


Persons_personal_dataLists.append({})
print(Persons_personal_dataLists)
Persons_personal_dataLists[5]={
    'Name':'Aybuk Pusat',
    'Age':30,
    'Course':'Graphic designer',
    'favHobbies':['Travelling','eating','Dancing','Acting'],
    'Country':'Turkiye'
}
print(Persons_personal_dataLists)


Persons_personal_dataLists.append({})
print(Persons_personal_dataLists)
Persons_personal_dataLists[6]={
    'Name':'Ayca Asin Turan',
    'Age':31,
    'Course':'IT',
    'favHobbies':['Travelling','Eating','Acting'],
    'Country':'Turkiye'
}
print(Persons_personal_dataLists)


Persons_personal_dataLists.append({})
print(Persons_personal_dataLists)
Persons_personal_dataLists[7]={
    'Name':'Berk Cankat',
    'Age':40,
    'Course':'IT',
    'favHobbies':['Travelling','Acting','Eating'],
    'Country':'Turkiye'
}
print(Persons_personal_dataLists)

#........Again Adding Methods......

Persons_personal_dataLists[5]['Religion']='Islam'
Persons_personal_dataLists[6]['Religion']='Islam'
Persons_personal_dataLists[7]['Religion']='Islam'
print(Persons_personal_dataLists)

Persons_personal_dataLists[5]['Country']='Egypt'
Persons_personal_dataLists[6]['Country']='Iran'
Persons_personal_dataLists[7]['Country']='France'
print(Persons_personal_dataLists)

Persons_personal_dataLists[5]['Id']=99861
Persons_personal_dataLists[6]['Id']=12300
Persons_personal_dataLists[7]['Id']=999043
print(Persons_personal_dataLists)


print(Persons_personal_dataLists[7].get('Name'))
print(Persons_personal_dataLists[7].get('favHobbies')[2])


#..........Finished!......#