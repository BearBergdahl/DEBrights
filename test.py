
foodlist = []
with open("food.txt") as myfile:
    foodlist = myfile.readlines()
foodstuff = set()
for line in foodlist:
    a, _ = line.split(':')
    foodstuff.add(a)

print(foodstuff)

raw_foodcount = len(foodlist)
foodcount = len(foodstuff)
print('total: ', raw_foodcount," and unique: " ,foodcount)

indexed_foodstuff = zip(range(foodcount), foodstuff)
food_dict = dict()
for each_tuple in indexed_foodstuff: 
    print(each_tuple)
    food_dict.update([each_tuple])

