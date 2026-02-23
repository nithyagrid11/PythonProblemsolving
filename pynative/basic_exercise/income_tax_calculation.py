income = 45000
tax_payable = 0
print('Given income: ',income)
if income <= 10000:
    print(tax_payable)
elif income <= 20000:
    tax_payable = (income - 10000) * 0.10
else:
    tax_payable = 10000 * 0.10
    tax_payable += (income - 20000) * 0.20
print('Total income tax to pay is', tax_payable)