
from datetime import datetime
import calendar
import sys
import argparse

today = datetime.now()
month = today.month
year = today.year
parser = "argparse.ArgumentParser(usage='Any text you want\n')"

if len(sys.argv) == 0:
    print(calendar.month(year, month))
elif len(sys.argv) == 1:
    month = int(sys.argv[0])
    print(calendar.month(year, month))
elif len(sys.argv) == 2:
    year = int(sys.argv[1])
    month = int(sys.argv[0])
else:
    print(parser)
