# Demo av listor, tupler och
# list(), string()



# Demo av pass by reference

spam = 'sausage'
egg = spam

#steg2
print(id(spam))
print(id(egg))

spam = 'bacon' # skapar en ny sträng

print(egg, spam)

print(id(spam))
print(id(egg))

spam = [1,2,3]
egg = spam
spam[2] = 7
print(egg)
print(spam)
print(id(spam))
print(id(egg))

import copy # dema med id()
import pprint

myDict = {'nyckel': 2, 'door':3, 'open':4}
for k in myDict.keys():
    print(k)
for item in myDict.items():
    print(item)
    print(type(item))

pprint.pprint(myDict)
print(myDict)

#string
#index, for, \n, \t
#r', f'

    




