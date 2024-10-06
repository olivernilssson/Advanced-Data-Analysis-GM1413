# Exercise 1.5: Portfolio Performance Analysis

def cumulative_returns(principal, return_rate, dividend_yield, years):
    return_rate = return_rate / 100
    dividend_yield = dividend_yield / 100
    for i in range(1, years + 1):
        principal = principal * (1 + return_rate) + principal * dividend_yield
    return round(principal, 2)


print(cumulative_returns(
    principal=float(input('Enter the principal amount: ')),
    return_rate=float(input('Enter the return rate [%]: ')),
    dividend_yield=float(input('Enter the dividend yield [%]: ')),
    years=int(input('Enter the number of years: ')
              )))
