#calculate avarge 

a = float(input("Enter the number1 :"))
b= float(input("Enter the number2 :"))

def avg(a,b):
    result = (a+b)/2
    
    return result
final= avg(a,b)
print("The Avarge is",final)

if final>10:
    print("good")
elif final==10:
    print("avarge")
    
else:
    print("bad")
    
list1 = {1,2,3,4,5,6}
sum = 0
for x in list1:
  sum = sum + x
  print(x,sum)       

    
