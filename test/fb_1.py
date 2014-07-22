# Get Args
import sys
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

# See if Arg is Valid for Use
num = 0
for i in range(len(sys.argv)):
    #print sys.argv[i]
    #num = sys.argv[i]
    try:
        n = int(sys.argv[i])
        if n <= 0:
          print "Must be at least 1"
        else:
          num = n
          print "Using arg[" + str(i) + "] = " + sys.argv[i]
          break
    except ValueError  as (strerror):
        #print "Not a valid integer."
        #print "Value Error: {}" .format (strerror)
        print "Ignoring arg[" + str(i) + "] = " + sys.argv[i]

# If no viable Arg, get Raw Input
if num == 0:
    # Get a valid number to count to
    while True:
        try:
            n = int(raw_input("Please enter an integer of at least 1: "))
            if n <= 0:
              print "Must be at least 1"
            else:
              break
        except ValueError  as (strerror):
            print "Not a valid integer."
            print "Value Error: {}" .format (strerror)
else:
    n = num

# Print numbers or substitutes
print "Fizz buzz counting up to " + str(n)
result = ""
for i in range(n):
  j = i + 1
  if j % 3 != 0 and j % 5 != 0:
    result += str(j)
  elif j % 3 == 0 and j % 5 == 0:
    result += "fizz buzz"
  elif j % 3 == 0:
    result += "fizz"
  else:
    result += "buzz"
  if j != n:
    result += ", "
print result