
#day_2_problem-7

input=15
for i in range(1,15+1):
 if i==1:
  print(i)
 elif i==2:
  print(i)
 elif i%3==0 and i%5==0:
    print("fizzbuzz")
 elif i%3==0:
     print("fizz")
 elif i%5==0:
    print("buzz")
 elif i%3!=0 and i%5!=0:
     print(i)         