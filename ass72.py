# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as
# shown below.
fname = raw_input('Enter file name: ')
try:
    fh = open(fname)
except:
    print 'wrong filename', fname
    exit()
count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count += 1
    total += float(line[line.find('0'):])
print 'Average spam confidence:', total / count
