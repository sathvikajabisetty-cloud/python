 for number in range(1,10):
     if number ==5:
         print("breaking the loop at number 5")
         break
     print(number)
    
 for i in range(0,10):
      if i%2==0:
         if i==2:
              break
         print(i)

 num =[3,5,6,7,8,9]
 for i in num:
     if i%2==0:
             print(i)
             break
 else:
     print("not") 
  
 while True:
  name = input("enter your name: ")
  if name =='sathvika':
     print("logined")
     break
  else:
     print("try again")
        
 for num in range(1,6):
     if num==3:
         print("skipping the num:3")
         continue
     print(num)

 list = (-1,-9,-8,1,2,3)
 for i in list:
     if i>0:
       print(i)

 list = (1,2,3,4,5,6,7,8,9)
 for i in list:
     if i%3==0:
         print("skipping num  ")
         continue
     print(i)
      
 for num in range(1,4):
    if num == 2:
     pass
    print(num)


