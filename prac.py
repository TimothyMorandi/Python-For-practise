"""A program to prompt the user for hours and rate per hour"""
hours = int(input("Enter the Hours worked: "))
rate_per_hour = float(input("Your rate per hour: "))
gross_pay = (hours * rate_per_hour)
print(f"Your Gross pay is{gross_pay} Ksh")