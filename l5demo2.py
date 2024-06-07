"""myDict = {'nyckel': 2, 'door':3, 'open':4}
for k in myDict.keys():
    print(k)
print(myDict.keys())
var1 = myDict.items()
for item in myDict.items():
    print(item)
    print(type(item))

for dictItem in var1:
    print(dictItem)
    print(type(dictItem))
my_nested_dict = {'movieName': 'Empire Strikes Back', 'actors':
                  [
                      {'actor':'Carrie Fisher', 'role':'Leia', 'episodes':{4:'A new Hope',5:'Empire Strikes Back',6:'The return of the Jedi',7:'Force awakens',8:'Last Jedi',9:'The rise of Skywalker'}}, 
                      {'actor':'Mark Hamill', 'role': 'Luke','episodes':{4:'A new Hope',5:'Empire Strikes Back',6:'The return of the Jedi',7:'Force awakens',8:'Last Jedi',9:'The rise of Skywalker'}},
                      {'actor':'Harrison Ford', 'role':'Han','episodes':{4:'A new Hope',5:'Empire Strikes Back',6:'The return of the Jedi',7:'Force awakens',8:'Last Jedi',9:'The rise of Skywalker'}} 
                  ]
                }
print(my_nested_dict) 
import pprint
pprint.pprint(my_nested_dict)
print('*************************************************')
myactors = my_nested_dict.get('actors')
pprint.pprint(myactors)
print(type(myactors))
"""

text = 'Min långa mening!'
print(text[0])
print(type(text))
charindex = text.index('!')
print(charindex)
text = 'min långa mening!'
capd = text.capitalize()
print(capd)
uppd = text.upper()
print(uppd)

mydir = r'Table header \trow1 \nrow2'
print(mydir)
my_names = ['Erika', 'Karin', 'Gonzalo', 'Jacob', 'Tobias']

for name in my_names:
    print('Hej ' +name+ ' kul att du är med på lektionen')
    print('Detta sätt skriver också ut %s namn' %(name))
    print(f'Den här varianten tillåter {name}-variabel {mydir} att inlinas i texten')

print('Hello'.islower())
