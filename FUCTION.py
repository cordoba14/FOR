# def myfunc():
#   print(" python is" + x)

# myfunc()

# x = " awesome"


# def myfunc():
#  x = "fantastic"
#   print(" python  is "  +  x)

# def greeting()
#    print("hello, are you")
#    print("my name is bogan")
#    print(" its is my pleasure to be working with you")

# greeting()
# print ("what if i want to greet someone else?")
# greeting()


#def greeting(name, sex):
 #   if sex == "m":
  #      prefix = "Mr."

   # elif sex == "f":
        #prefix = "Mrs."

    #else:
     #   prefix = ""

    #print("hello {} {}, are you".format(prefix, name))
    #print("my name is bogan")
    #print(" its is my pleasure to be working with you")


#Person = input("who do you want to greet")
#prefix = input("sex")
#greeting(Person, prefix)
#print("what if i want to greet someone else?")

#greeting(Person, prefix)


fp = open ( "ols")
list = []
fp.contents = fp.read()
line =  " "
punct = ",- , ."
for p in fp.contents:
    if p not in punct:
      line = line + p


line = line.split()

for x in line:
     if x not in list:
      list.append(x)


print(" Harry poter has ", len (list), " unique word")







#fp2.write(line.replace(p, " "))
































        #call the split method on line
        #if x in list:




