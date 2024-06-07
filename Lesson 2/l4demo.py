#collatz

print('Give me a number:')
number = int(input())

def collatz(num):
    while not num == 1:
        print(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3 +1
    print(num)



#CollatzSequence
def collatz_r(num):
    if num == 1:
        print(num)
    elif num % 2 == 0:
        print(num)
        num = num // 2
        collatz(num)
    else:
        print(num)
        num = 3 * num + 1
        collatz(num)

collatz(number)
collatz_r(number)

dogNames = []

while True:
    print('Enter a dog name for dog number ' + str(len(dogNames)+1) +
          ' (Or type enter to quit.):' )
    name = input()
    if not name:
        break
    dogNames = dogNames + [name]
print('The dogs are named: ')
for index, name in enumerate(dogNames):
    print('Dog number: ' + str(index+1) + ' ' + name)


my_list = [3,4,5,7,8,9,11,2,4,1,2,5,3,99,0]
    
if 4 in my_list:
    print('It´s there!')
if 6 not in my_list:
    print('It´s not there!')

myDogNames = ['Abby', 'Moody', 'Fido']
dog1, dog2, dog3 = myDogNames
print(dog1, dog2, dog3)

def testList():
    
    var2 = 3
    
    var4 = 1
    return [var2, var4]

myNetflix = testList()

season_nr, ep_nr = myNetflix
print('Next is season: ' +str(season_nr)+ ' episode: ' + str(ep_nr))

my_List = [3,4,5,6,7,8,9,12,22,33,51]
my_List.append(2)
my_List.insert(7,911)
print(my_List.index(4))
my_List.remove(22)
for item in my_List:
    print(item)

words = ['horse', 'donkey', 'cow', 'sheep', 'Cow']

def returnWord(word):
    if word in words:
        word_index = words.index('cow')
        returnWord = words[word_index]
        words.remove(word)
        return returnWord
    else:
        return ''

wordToFind = input('What word do you seek?')
if returnWord(wordToFind):
    print(wordToFind + ' was there and is removed now')
else:
    print(wordToFind + ' was not in list')

print(words.index('cow'))
words.sort()
print(words.index('cow'))
for word in words:
    print(word)

nums = [5,3,7,1,99,3,4,77,1,3,4,555,6,3,77,4,8,44,2,0,1111,23]
nums.remove(3)
for num in nums:
    print(num)
nums.sort()
for num in nums:
    print(num)
    
    



