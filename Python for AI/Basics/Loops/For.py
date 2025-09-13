for i in range(5):   # range(5) → 0,1,2,3,4
    print(i)
print(f"\n")

#Iterating over a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print(f"\n")
#Iterating over dictionary:
person = {"name" : "Ada Lovelace", "age" : 27}
for key, value in person.items() :
    print(f"{key} : {value}")
print(f"\n")

for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("Loop finished without break")  # won’t run here


while i in fruits :
    print(i)