thislist =["hello", "hii", "subaru","bruce"]
mylist = [x.upper() if x != "bruce" else "nigger" for x in thislist ]
print(type(thislist))
mylist1 = mylist.copy()
mylist2 = mylist[:]
mylist3 = list(mylist)
mylist4 = thislist
print(mylist)


mylist.sort(key = str.lower) #sort is case senstive
mylist1.sort(reverse=True)
mylist2.sort()
print(mylist)
print(mylist1)
print(mylist4)

another = ["apple", "banana", "smoke"]
thislist.extend(another)
print(thislist)
another.clear()
print(another)

for x in range(1,11):
    another.append(x)
    print(another)
 

another1 = another.copy()

# another.pop(2)
# print(another)
# del another[2]
# print(another)
# another.remove(2)
# print(another)

for x in range(len(another1)):
    print(another1)
    another1.pop()
