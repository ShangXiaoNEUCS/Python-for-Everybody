# Shang Xiao solution for 3.1

hrs = input("Enter Hours:")
rat = input("Enter Rate:")
h = float(hrs)
r = float(rat)
if h>40:
    print ((h-40)*1.5*r+40*r)