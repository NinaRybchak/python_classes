balance = float(input("balance = "))
annualInterestRate = input("annualInterestRate = ")
monthlyInterestRate = float(annualInterestRate) / 12.0
monthly_lower_bound = balance / 12
i = 1
max_balance = balance
for i in range(1,13):
    max_balance = max_balance + monthlyInterestRate * max_balance
monthly_upper_bound = max_balance / 12.0
monthlyLowestPayment = (monthly_lower_bound + monthly_upper_bound) / 2
remainingBalance = balance
while monthly_upper_bound - monthly_lower_bound >= 0.01:
    remainingBalance = balance
    for i in range(1,13):
        remainingBalance = remainingBalance - monthlyLowestPayment
        remainingBalance = remainingBalance + monthlyInterestRate * remainingBalance
    if remainingBalance > 0:
        monthly_lower_bound = monthlyLowestPayment
    elif remainingBalance < 0:
        monthly_upper_bound = monthlyLowestPayment
    monthlyLowestPayment = (monthly_lower_bound + monthly_upper_bound) / 2
print("Lowest Payment: " + str(round(monthlyLowestPayment,2)))
print("Overpayment is: " + str(abs(round(remainingBalance, 2))))
