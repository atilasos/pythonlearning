x="nao"
while x.strip() != 'sim':
    inp=raw_input("EUR floor?")
    usf=int(inp)+1
    print "US floor", usf
    x=raw_input("sair?")
print ('out of while')
