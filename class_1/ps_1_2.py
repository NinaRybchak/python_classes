balance = float(input("balance = "))
annualInterestRate = input("annualInterestRate = ")
monthlyInterestRate = float(annualInterestRate) / 12.0
monthlyPaymentRate = float(input("monthlyPaymentRate = "))
minimumPayment = 0
remainingBalance = balance
i = 1
while i <= 12:
    minimumMonthlyPayment = remainingBalance * monthlyPaymentRate
    remainingBalance = remainingBalance - minimumMonthlyPayment
    remainingBalance = remainingBalance + monthlyInterestRate * remainingBalance
    print("Month: " + str(i))
    print("Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2)))
    print("Remaining balance: " + str(round(remainingBalance, 2)))
    minimumPayment += minimumMonthlyPayment
    i += 1
print("Total paid: " + str(round(minimumPayment, 2)))
print("Remaining balance: " + str(round(remainingBalance, 2)))
