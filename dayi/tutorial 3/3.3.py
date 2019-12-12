sentence1 = "@num tax on a Chocolate cake costing $17.50 is @momey."
sentence1.spilt()
GST = ["5%","10%","15%","20%","25%"]
def GSTmoney(num,money):
    Discount = sentence1.replace("@num",num)
    Discount = sentence1.replace("@money",money)
    print(Discount)
for s in GST:
    GSTmoney(sentence1,"(GST*17.5)/100")
