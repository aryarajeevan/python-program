#sum of even numbers up to n
limit=int(input("enter the limit"))
sum=0
for i in range(1,limit+1):
  n=int(input())
  if n%2==0:
    sum=sum+n
print("sum is : ",sum)
