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

def is_loan_eligible(employment_type, age, salary, loan_period):
    """
    Determines if an individual is eligible for a home loan based on employment type, age, salary, and loan tenure.

    Parameters:
    employment_type (str): The employment type of the individual ('salaried' or 'self-employed').
    age (int): The age of the individual.
    salary (int): The annual salary of the individual.
    loan_period (int): The requested loan tenure in years.

    Returns:
    bool: True if eligible for the loan, False otherwise.
    """
    MAX_AGE_LIMIT = 58
    MIN_SALARY_SALARIED = 120000
    MIN_SALARY_SELF_EMPLOYED = 200000

    if not (employment_type in ['salaried', 'self-employed']):
        return False

    if age + loan_period > MAX_AGE_LIMIT:
        return False

    if (employment_type == 'salaried' and salary >= MIN_SALARY_SALARIED) or \
       (employment_type == 'self-employed' and salary >= MIN_SALARY_SELF_EMPLOYED):
        return True

    return False

def main():
    """
    Main function to take user input and print loan eligibility status.
    """
    employment_type = input("Enter your employment type (salaried/self-employed): ")
    age = int(input("Enter your age: "))
    salary = int(input("Enter your annual salary: "))
    loan_period = int(input("Enter desired loan tenure (in years): "))

    if is_loan_eligible(employment_type, age, salary, loan_period):
        print('Eligible')
    else:
        print('Not eligible')

if __name__ == "__main__":
    main()
