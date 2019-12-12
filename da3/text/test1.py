# test1
# print("caterpillar"[:])
# print("caterpillar" * 5)
# print("caterpillar"[0:11:2])
# print(list("caterpillar").pop())
#
#
# def ret(list1):
#     for i in list1:
#         if list(i)[0] == 'a':
#             print(i)
#
# ret(["aa","oo","as"])


# def f(x):
#     thelist = list(x)
#     print(thelist[-1:])
#     thelist[-1:] = list("ing")
#     return "".join(thelist)
# for s in ["breathe", "hike", "drive", "dive"]:
#     print(f(s))


class colourlist:
    def __init__(self):
        self.colours = []
        self.length = 0

    def __str__(self):
        liststring = ""
        for c in self.colours:
          liststring = liststring + c + " "
        return liststring

    def addcolour(self,colour):
        self.colours.append(colour)
        # print(self.colours)
        
    def countcolour(self):
        colour = self.colours
        s = []
        for i in colour:
            if s == []:
                s.append(i)
            else :
                for j in s:
                    if j != i:
                        s.append(i)
        print(s,"ppp")
        for a in s:
            print(a, ":", colour.count(a))

c = colourlist()
c.addcolour("sss")
c.addcolour("ppp")
c.addcolour("sss")
c.addcolour("sss")
c.addcolour("sss")
c.addcolour("sss")
c.addcolour("sss")
c.addcolour("dsadad")
c.countcolour()