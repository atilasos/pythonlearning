def computepay(h,r):
    if h > 40:
        pay = (h-40)*(1.5*r)+(40*r)
    else:
        pay = h*r
    return pay
hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
hrs = float(hrs)
rate = float(rate)
print computepay(hrs,rate)
