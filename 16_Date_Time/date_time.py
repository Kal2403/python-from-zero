# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

from date_time import datetime

# current date and time
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("TimeStap:", timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.

date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print("Converted date:", converted_date)

# 4. Calculate the time difference between now and new year.

new_year = datetime(year + 1, 1, 1)
diffrence_new_year = new_year - now
print("Time until new year:", diffrence_new_year)

# 5. Calculate the time difference between 1 January 1970 and now.

epoch = datetime(1970, 1, 1)
diffrence_epoch = now - epoch
print("Time since 1 January 1970:", diffrence_epoch)

# 6. Think, what can you use the datetime module for? Examples: Time series analysis, To get a timestamp of any activities in an application, Adding posts on a blog

# Python DateTime

# Getting datetime info

from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formatting Date Output Using strftime

from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

from datetime import date

d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())
# date object of todays date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

# Time Objects to Represent Time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555

# Difference Between Two Points in Time Using

from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# Difference Between Two Points in Time Using timedelta

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)