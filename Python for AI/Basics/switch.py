
while True:
 op = int(input(f"enter the operation\n 1- running sum \ 2- check if its a power of 2 \ 3 - addition \n 4-exit :   "))
 sum =0
 match op:
    case 1:
        while True :
            num1 = int(input("Enter the number: "))
            if num1!=-1:
              sum = sum + num1
            else :
              print(sum)
              break    

    case 2:
        num1 = int(input("Enter the first number: "))
        if num1<0 :
            print("nuh uh")
        else :
           while(num1%2==0) :
              num1 = num1/2

           if(num1==1) :
              print("Is a power of 2")
           else: 
              print("nope")
    case 3:
      num1 = int(input("enter teh frist number:"))
      num2 = int(input("deadsas: "))
      print(num1+num2)
    
    case 4:
       break

    case _:
      print("dont be reatrad")  
                          

