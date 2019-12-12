s=0
i=1
while i<11:
    if i==3:
       i=i+1
       continue
    else:
      a=i**3
      print(i,"      ",a)
      s=s+a
      i=i+1
print("total:",s)
