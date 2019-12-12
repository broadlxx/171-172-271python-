def readlines(inputFilename):
    file1=open(inputFilename,'r')
    lines=file1.readlines()
    file1.close()
    return lines

def creatSubsetOfLines(lines,OmitFromStart,OmitFromEnd):
    Len=len(lines)
    shorterlines=[]
    if Len<OmitFromStart+OmitFromEnd:
        print("Omit too long")
    else:
        for i in lines[OmitFromStart:Len-OmitFromEnd]:
            shorterlines.append(i)
    return shorterlines

def writeToFile(shorterList):
    newfile=open(file,'w')
    for i in shorterList:
        newfile.write(i)
    newfile.close()

try:
    print(" *** Truncating File Copy ***")
    OmitFromStart = int(input("Omit how many lines from the start:"))
    OmitFromEnd = int(input("Omit how many lines from the end:"))
    inputFilename=input("The known file name and format is:")
    file=input("The new file name and format is:")
    lines=readlines(inputFilename)
    shorterList=creatSubsetOfLines(lines,OmitFromStart,OmitFromEnd)
    writeToFile(shorterList)
except:
    print("Don`t have file")





