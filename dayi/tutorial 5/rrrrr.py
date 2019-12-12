start = int(input("A start value:"))
for i in range(start*2-1):
    print("○",end="")
print()
for t in range(start-1):
      print("○",end="\t")
      for j in range(start-2):
          print(" ",end="\t")
      print("○")
for i in range(start*2-1):
     print("○",end="")
