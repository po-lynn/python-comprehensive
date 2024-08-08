import datetime

t = datetime.time(5,25,1)
print(t)
print(t.hour)
print(datetime.time.min)
print(datetime.time.max)
today = datetime.date.today()

print(today)

print(today.timetuple())
d1 = datetime.date(2023,3,17)
d2 = datetime.date(2023,2,17)

import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get the date and time for a specific moment
dt = datetime.datetime(2023, 3, 17, 15, 30, 0)
print("Specific date and time:", dt)

# Get the date and time components separately
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Format the date and time as a string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted)

