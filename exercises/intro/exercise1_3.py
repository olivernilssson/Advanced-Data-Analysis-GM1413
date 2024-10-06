# Exercise 1.3: Compound Interest

def compound_interest(principal, rate, years):
    rate = rate / 100
    return round(principal * (1 + rate) ** years, 2)


print(compound_interest(
    principal=float(input('Enter the principal amount: ')),
    rate=float(input('Enter the interest rate [%]: ')),
    years=int(input('Enter the number of years: ')
              )))
