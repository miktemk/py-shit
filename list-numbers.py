# Generates a printout of date stamps for the next year. Whoof!
# For more date formatting check out the [documentation](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

import sys, os, re
import time, datetime

for i in range(100):
	print (str(i+1) + ", ", end="")
