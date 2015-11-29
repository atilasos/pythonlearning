# 8.4 Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() function. The
# program should build a list of words. For each word on each line check
# to see if the word is already in the list and if not append it to the
# list. When the program completes, sort and print the resulting words in
# alphabetical order.
fname = raw_input('Enter file name: ')
try:
    fh = open(fname)
except:
    print 'wrong filename', fname
    exit()
lst = list()
lstfinal = list()
for line in fh:
    lst = line.split()
    for word in lst:
        if word in lstfinal:
            continue
        lstfinal.append(word)
lstfinal.sort()
print lstfinal
