#armstong number checking
n=input("enter a number")
num=int(n)
sum=0
ex=len(str(num))
print(ex)
for i in (n):
  sum=sum+int(i)**ex
if num==sum:
  print(num,"is an armstrong number")
else:
  print(num,"is not an armstrong number")

