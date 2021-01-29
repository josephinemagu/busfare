from datetime import date
from datetime import datetime
import locale

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
# get the current date and time

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%a")
print("date and time =", dt_string)

# Taken day number from user

if dt_string == "Mon" or "Tue" or "Wed" or "Thu" or "Fri":
    print("\n Bus fare is 100");

elif dt_string== "Sat":
    print("\n Bus fare is 60")
else:
    print("\n Bus fare is 80.")


