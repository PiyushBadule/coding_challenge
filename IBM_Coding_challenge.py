# Loan Eligibility Calculator
# Buying a house is a dream for most of us. Bank offer home loans to fulfil such dreams.When banks offer home
# loan, it does eligibility check on the financial status of the individual to determine his repay ability.
# If the individual financial status meets the bank's requirement, then it provides home loan, otherwise it
# denies. If the loan is provided, then the individual pays EMI for the loan term period of say x years which
# interest & thus he repays the loan at the end of loan term period.
# Give the type of employment age, annual salary & loan tenure, here we have to determine whether the person
# meets the loan conditions & he is eligible to apply for home loan or not.

#The condition to follows:
# 1. Type of employment can be salaried or self-employed
# 2. Age limit for the Individuals 21 to 58 years
# 3. Minimum Salary for Salaried employee is 120000 per annum
# 4. Minimum salary for Self-Employed individuals is 200000 per annum

# Sample Test Case 1             Sample Test Case 2
# self-employed                  salaried
# 32                             29
# 180000                         300000
# 20                             25

employment_type = input()
age = int(input())
salary = int(input())
loan_period = int(input())
if employment_type == 'salaried' or employment_type == 'self-employed':
    if age + loan_period <= 58:
        if employment_type == 'salaried' and salary >= 120000:
            print('Eligible')
        elif employment_type == 'self-employed' and salary >= 200000:
            print('Eligible')
        else:
            print('Not eligible')
    else:
        print('Not eligible')
else:
    print('Not eligible')