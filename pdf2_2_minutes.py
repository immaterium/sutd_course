def minutes_to_years_days(mins):
    days = (mins//60)//24
    years = days // 365
    days = days % 365
    return years, days

mins = int(input("Enter the number of minutes:"))
years, days = minutes_to_years_days(int(mins))
print("{:d} minutes is approximately {:d} years and {:d} days".format(mins, years, days))