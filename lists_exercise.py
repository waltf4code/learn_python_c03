# Lists - Exercise
# Selling Lemonade

# - You sell limonade over two weeks, the lists show number of lemonades sold per week
# - Profit for each lemonde sold is 1.5$
# Add another day to week 2 list  by capturing a number input
# Combine the two lists into the list called 'sales'
# Calculate/ print how much you have earned on
# Best day
# Worst day
# Separately and in total
# Hint: 3 print in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales.append(int(new_day))
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()

worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit: $ {worst_day_prof + best_day_prof}')