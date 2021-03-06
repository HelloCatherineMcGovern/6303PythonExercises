# create a function to calculate various taxes for an employee
# see instructions for details

def calc_payroll_tax(gross_pay_input):
    gross_pay = float(gross_pay_input)
    medicare = gross_pay * 0.0145
    futa = gross_pay * 0.006
    ss_tax_employer = gross_pay * 0.062
    ss_tax_employee = gross_pay * 0.062
    total_tax = medicare + futa + ss_tax_employee
    net_pay = gross_pay - total_tax
    print(f"Gross Pay: $ {gross_pay:.2f}")
    print(f"Medicare Tax: $ {medicare:.2f}")
    print(f"FUTA Tax: $ {futa:.2f}")
    print(f"Social Security Tax paid by Employer: $ {ss_tax_employer:.2f}")
    print(f"Social Security Tax paid by Employee: $ {ss_tax_employee:.2f}")
    print(f"Net Pay: $ {net_pay:.2f}")
