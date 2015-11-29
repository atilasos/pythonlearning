"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
lst = list()
names = dict()
biguser = None
bigcount = None
# Take care of filename and user input error's
fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fh = open(fname)
except:
    print 'wrong filename', fname
    exit()
# populate lst with the emails
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    lst.append(words[1])
# populate names with the email and the count
for ppl in lst:
    names[ppl] = names.get(ppl, 0) + 1
# find the most prolific commiter
print lst
for user, count in names.items():
    if biguser is None or count > bigcount:
        biguser = user
        bigcount = count
print biguser, bigcount
