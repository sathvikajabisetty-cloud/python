A = int(input("enter the value of side 1: "))
B = int(input("enter the value of side 2: "))
C = int(input("enter the value of side 3: "))
if A==B==C:
    print("equilateral triangle")
if( A==B!=C or A!=B==C or A==C!=B):
    print("isoceles triangle")
else:
    print("scalene triangle")

