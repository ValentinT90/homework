my_dict={'Valentin': 1990, 'Aleksandra': 1997,'Daria': 2019}
print(my_dict)
print(my_dict['Valentin'])
print(my_dict.get('Valera'))
my_dict.update({'Olga': 2020,'Pavel': 2018})
a=my_dict.pop('Aleksandra')
print(a)
print(my_dict)

my_set={1,2,3,4,5,5,3,1,'Bananas',True,(1,2,3)}
print(my_set)
(my_set.add(7))
(my_set.add(8))
(my_set.remove(1))
print(my_set)