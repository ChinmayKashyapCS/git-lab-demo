l=[2,4,9,3,1]
l.sort()
e=1
c=0
a=0
b=len(l)-1
mid=(a+b)//2
while(a<=b and a<=mid and b>=mid):
  mid=(a+b)//2
  if l[mid]==e:
      c=1
      break
  elif l[mid]>e:
      b=mid-1
  elif l[mid]<e:
      a=mid
  if e in l:
      c=1
      break
if c==1:
  print("Found")
elif c==0:
  print("Not found")
