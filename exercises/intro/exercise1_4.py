# Exercise 1.4: Analysing Monthly Sales Data

# List containing the sales digures for each month
sales_figures = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]


def average_sales(sales_figures):
    return sum(sales_figures) / len(sales_figures)


def max_sales(sales_figures):
    return max(sales_figures)


def min_sales(sales_figures):
    return min(sales_figures)


print(f'Average sales: {average_sales(sales_figures)}')
print(f'Maximum sales: {max_sales(sales_figures)}')
print(f'Minimum sales: {min_sales(sales_figures)}')
