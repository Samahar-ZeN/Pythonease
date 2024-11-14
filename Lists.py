#................1
#.............Data Types......
#.......Lists......
#......Lists/Arrays.......
#....But we call arrays asa alist in Python Language......

#..............1

my_namesLists=['Samahar','Ozge','Berk','Burak','Hande','Ayca','Furkan','Aybuk','Burak','Burak']
print(my_namesLists)
for i in my_namesLists:
    print(i)



#.......Methods of  Lists:......
#......method#1.......
#......Append method........

fruits_namesList=['Mangoes','Oranges','Kivi','Grapes','Pineapple']
fruits_namesList.append('Strawberry')
fruits_namesList.append('Apple')
fruits_namesList.append('Bananas')
for i in fruits_namesList:
    print(i)


#............method#2......
#.........Clear Method.....

my_subj_namesList=['Math','Computer','English','Urdu','Islamiyat','Economics','Education','Civics']
my_subj_namesList.clear()
for i in my_subj_namesList:
    print(i)

#.......Method#3.....
#.......Extend Method..........

my_fav_programminglang_namesLists=['Python','Js','PHP','Java','SQL','Ruby']
my_fav_programminglang_namesLists.extend('C++')
my_fav_programminglang_namesLists.extend('React')
for i in my_fav_programminglang_namesLists:
    print(i)

#.........Method4....
#.......Count Method.....

my_namesLists=['Samahar','Ozge','Berk','Burak','Hande','Ayca','Furkan','Aybuk','Burak','Burak']
let_a=my_namesLists.count('Aybuk')
let_a=my_namesLists.count('Burak')
print(let_a)
for i in my_namesLists:
    print(i)



#...............Method#5..........
#............insert Method........

my_fav_countries_namesLists=['Turkiye','America','Egypt','Uk','England','Iran','Azerbijan','Austrailia']
my_fav_countries_namesLists.insert(1,'Qatar')
my_fav_countries_namesLists.insert(4,'Iraq')
my_fav_countries_namesLists.insert(6,'Sirilanka')
my_fav_countries_namesLists.insert(7,'Paris')
my_fav_countries_namesLists.insert(3,'Yemen')
for i in my_fav_countries_namesLists:
    print(i)


#.......Method#6.......
#........'Reverse Method'........

fruits_namesList=['Mangoes','Oranges','Kivi','Grapes','Pineapple']
fruits_namesList.reverse()
for i in fruits_namesList:
    print(i)


#......Method#7........
#......Sort Method.....

my_fav_programminglang_namesLists=['Python','Js','PHP','Java','SQL','Ruby']
my_fav_programminglang_namesLists.sort()
for i in my_fav_programminglang_namesLists:
    print(i)

#.........Method#8......
#.........Pop Method....

fruits_namesList=['Mangoes','Oranges','Kivi','Grapes','Pineapple']
let_b=fruits_namesList.pop(4)
let_b=fruits_namesList.pop(2)
print(let_b)
for i in fruits_namesList:
    print(i)


#..........Method#9......
#.......remove Method......

my_subj_namesList=['Math','Computer','English','Urdu','Islamiyat','Economics','Education','Civics']
my_subj_namesList.remove('Civics')
my_subj_namesList.remove('Urdu')
my_subj_namesList.remove('Education')
for i in my_subj_namesList:
    print(i)


#.......Method#10....
#........Index Method.....

my_namesLists=['Samahar','Ozge','Berk','Burak','Hande','Ayca','Furkan','Aybuk','Burak','Burak']
let_i=my_namesLists.index('Aybuk')
let_i=my_namesLists.index('Furkan')
let_i=my_namesLists.index('Berk')
let_i=my_namesLists.index('Burak')
print(let_i)
for i in my_namesLists:
    print(i)

#......Method11...
#.....copy Method....

my_fav_programminglang_namesLists=['Python','Js','PHP','Java','SQL','Ruby']
my_fav_programminglang_namesLists.copy()
for i in my_fav_programminglang_namesLists:
    print(i)


#.........Finished!........#