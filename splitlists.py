def splitlist(a):
    if len(a) > 1:
        alist = a[0:len(a)/2]
        blist = a[len(a)/2:]
        splitlist(alist)
        splitlist(blist)
        i = 0
        j = 0
        k = 0
        while i < len(alist) and j < len(blist):
            if alist[i] < blist[j]:
                a[k] = alist[i]
                i += 1
            else:
                a[k] = blist[j]
                j += 1
            k += 1
        while i < len(alist):
            a[k] = alist[i]
            i += 1
            k += 1
        while j < len(blist):
            a[k] = blist[j]
            j += 1
            k += 1
    print a
# start using
fname = 'mbox-short.txt'
count = 0
total = 0
lst = list()
fh = open(fname)
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count += 1
    total += float(line[line.find('0'):])
    lst.append(float(line[line.find('0'):]))
splitlist(lst)
