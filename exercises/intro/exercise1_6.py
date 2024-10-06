# Exercise 1.6: Cash Flow Analysis and Net Present Value (NPV) Calculation

def npv(rate, years):
    rate = rate / 100
    cash_flows = []
    npv_value = 0

    for i in range(1, years + 1):
        while True:
            try:
                cash_flow = float(input(f'Enter cash flow for year {i}: '))
                cash_flows.append(cash_flow)
                npv_value += cash_flow / (1 + rate) ** i
                break
            except ValueError:
                print(f"Invalid input! Please enter a valid number for cash flow for year {i}.")

    return round(npv_value, 2), min(cash_flows), max(cash_flows)


# Get inputs and calculate NPV, min and max cash flows
try:
    rate = float(input('Enter the discount rate [%]: '))
    years = int(input('Enter the number of years: '))

    npv_value, min_cash_flow, max_cash_flow = npv(rate, years)

    print(f"\nResults:")
    print(f"Net Present Value (NPV): {npv_value}")
    print(f"Minimum Cash Flow: {min_cash_flow}")
    print(f"Maximum Cash Flow: {max_cash_flow}")

except ValueError:
    print("Invalid input! Please enter a valid number for rate and years.")
