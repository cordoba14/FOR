#equals a ==b
#not equals : a !=b
#less tan: a < b
# less tan or equal to: a<=b
# greater than: a > b
# greater tha or equal to: a> = b
#these conditions above can be used in several ways, mostly commonly in "if statements" and lopps-

a = 33
b = 200
if b > a:
    print(" b is greater tha a")

#Indentation python relies on indentation ( whitespace at the beginning of a line) to define scope
# in this code.


#elif: the elif keyword is pythons way of sayin " is the previos conditions were not true
#then try this condition

a = 33
b = 33
if b > a:
    print( "b is greater than a ")

elif a == b:
    print("a and b are equal")

# in this example a is equal to b, so the first condition is no true, but the elif condition is true so weprint
#to screen that that " and b are equal"

#Else
# the else keyword catches anything wich isn´t caught by the preceding conditios

a = 200
b = 33

if b > a:
    print ("b is greater than a")
elif a == b:
    print ( "b is greater than a")
else:
    print (" a is greater tan b")



