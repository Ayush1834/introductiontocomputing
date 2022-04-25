Standard_Deduction=10000
Dependent_Deduction=3000
Dependents=int(input("Enter the number of dependents"))
Total_Deduction=Standard_Deduction+(Dependent_Deduction*Dependents)
print("Total Deduction is",Total_Deduction)
Gross_Income=float(input("Enter your gross income"))
Total_Taxable_Amount=Gross_Income-Total_Deduction
print("Total Taxable amount is ",Total_Taxable_Amount)
Total_Tax=0.2*Total_Taxable_Amount
print("Total Tax is",Total_Tax)
