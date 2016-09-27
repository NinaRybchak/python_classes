balance = float(input("balance = "))
annualInterestRate = input("annualInterestRate = ")
monthlyInterestRate = float(annualInterestRate) / 12.0
remainingBalance = balance
monthlyLowestPayment = 10
while True:
    i = 1
    while i <= 12:
        remainingBalance = remainingBalance - monthlyLowestPayment
        remainingBalance = remainingBalance + monthlyInterestRate * remainingBalance
        i += 1
    if remainingBalance > 0:
        monthlyLowestPayment += 10
        remainingBalance = balance
    else:
        break
print("Lowest Payment: " + str(monthlyLowestPayment))
print("Overpayment is: " + str(abs(round(remainingBalance, 2))))
