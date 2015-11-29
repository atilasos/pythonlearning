"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
# Take care of filename and user input error's
fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fh = open(fname)
except:
    print 'wrong filename', fname
    exit()
# populate lst with hours
lst = list()
for line in fh:
    if not line.startswith('From '):
        continue
    lst.append(line[:line.find(':')].split()[5])
# populate hours with the hour and the count
hours = dict()
for hour in lst:
    hours[hour] = hours.get(hour, 0) + 1
# sorting hours
time = sorted([(time, hour) for time, hour in hours.items()])
for h, c in time:
    print h, c
