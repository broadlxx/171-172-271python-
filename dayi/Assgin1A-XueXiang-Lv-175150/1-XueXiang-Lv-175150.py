print("XueXiangLv 175150")
def num(loan_amount,number_of_weeks):
    S = loan_amount/number_of_weeks
    return S
loan_amount = float(input("How mach do you borrow:"))
number_of_weeks = int(input("How long do you need repay"))
print("Enter an amount",loan_amount)
print("Enter a number",number_of_weeks)
print("You must repay $",num(loan_amount,number_of_weeks) ," per week to repay a loan of $",loan_amount,"in",
number_of_weeks,"weeks")
