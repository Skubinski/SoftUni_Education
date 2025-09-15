# Define constants for conversions
DAYS_IN_YEAR = 365.2422
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

# Input: Read an integer number of centuries
centuries = int(input())

# Calculate the equivalent years, days, hours, and minutes
years = centuries * 100  # Each century has 100 years
days = int(years * DAYS_IN_YEAR)  # Convert to an integer for days
hours = days * HOURS_IN_DAY
minutes = hours * MINUTES_IN_HOUR

# Display the result
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
