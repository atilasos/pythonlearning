def splitlist(a,b,c,d):
    if len(a) >= 2:
        splitlist(a[0:len(a)/2],a[len(a)/2:],c,d)
        if len(a) <= 3 and a[0] <= a[1]:
            temp=c[0]
            c[0]=a[0]
            if a[1] <= temp:
                c.expand(a[1])
            else:
                c.expand(temp)
        elif len(a) == 1 and a[0] <= c[0]:
            temp=c[0]
            c[0]=a[0]
            c.expand(temp)
        else: print c
    print c

fname = 'mbox-short.txt'
count = 0
total = 0
lst = list()
fh = open(fname)
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    count +=1
    total += float(line[line.find('0'):])
    lst.append(float(line[line.find('0'):]))
Alist=lst[0:len(lst)/2]
Blist=lst[len(lst)/2:]
Clist=list()
Dlist=list()
splitlist(Alist,Blist,Clist,Dlist)
