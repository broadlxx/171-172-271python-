Balance = 0
def setBalance(amt):
    global Balance
    Balance=amt
def printBalance():
    # global Balance
    print("Current Balance is $ %5.2f"%(Balance))
def printLedgerLine(date, amount, details):
    # global Balance
    print("%10s      %-18s $%8.2f        $%8.2f "%(date, details, amount,Balance))
def deposit (date, details, amount):
    global Balance
    Balance = Balance+amount
    printLedgerLine(date, amount, details)
def withdraw(date, details, amount):
    global Balance
    Balance=Balance-amount
    printLedgerLine(date, amount, details)
setBalance(500)
printBalance()
withdraw("17-12-2012", "BP - petrol", 72.50)
withdraw("19-12-2012", "Countdown", 55.50)
withdraw("20-12-2012", "munchies", 1.99)
withdraw("22-12-2012", "Vodafone", 20)
deposit ("23-12-2012", "Income", 225)
withdraw("24-12-2012", "Presents", 99.02)
printBalance()
