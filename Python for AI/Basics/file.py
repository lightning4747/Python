import os

with open("sample.txt", "x") as f:
   print("nigger")

with open("sample.txt", "rt") as f:
    print(f.read())

with open ("sample.txt", "a") as f :
    f.write("nigger")    

with open("sample.txt","r") as f:
 print(f.read())    

# os.remove("sample.txt") 
os.remove("file.py")