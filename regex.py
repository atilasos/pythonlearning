import re
# Take care of filename and user input error's
fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'regex_sum_202730.txt'
try:
    fh = open(fname)
except:
    print 'wrong filename', fname
    exit()
allfile = fh.read()
allnumbers = re.findall('\D*(\d+)\D+?', allfile)
sumall = 0
for number in allnumbers:
    sumall += int(number)
print sumall
