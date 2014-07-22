import sys

def main(argv):  
    print "Testing Sub Function Argument Validation"
    num = GetIntegerArgument(argv)
    # Proceed With Valid Argument or Get Valid Input
    if num > 0:
        print "Found Valid Number: " + str(num)
    else:
        # Demand Postive Integer, Raw Input
        print "Testing Sub Function Input Validation"
        num = GetIntegerInput()
        print "Found Valid Number: " + str(num)
    # Run FizzBuzz
    FizzBuzz(num)
            
def GetIntegerArgument(args):   
    """Get a valid number argument, if any"""
    num = 0
    for i in range(len(args)):
        try:
            n = int(args[i])
            if n <= 0:
              print " Must be at least 1"
            else:
              num = n
              print " Using arg[" + str(i) + "] = " + args[i]
              break
        except ValueError  as (strerror):
            print " Ignoring arg[" + str(i) + "] = " + args[i]
    return num
            
def GetIntegerInput():
    """Get a valid number as input"""
    while True:
        try:
            n = int(raw_input(" Please enter an integer of at least 1: "))
            if n <= 0:
              print "  Must be at least 1"
            else:
              break
        except ValueError  as (strerror):
            print "  Not a valid integer."
            print "  Value Error: {}" .format (strerror)
    return n

def Divisible(x,y):
    """ This SubFunction is a waste of time. It creates more work than it saves. """
    if x % y == 0:
        return True
    else:
        return False

def FizzBuzz(n):
    """Do the Fizz Buzz Counting Thing"""
    print "Fizz buzz counting up to " + str(n)
    result = ""
    for i in range(n):
      j = i + 1
      if not Divisible(j,3) and not Divisible(j,5):
          result += str(j)
      elif Divisible(j,3) and Divisible(j,5):
          result += "fizz buzz"
      elif Divisible(j,3):
          result += "fizz"
      else:
          result += "buzz"
      if j != n:
          result += ", "
    print result

# Main Function
if __name__ == "__main__":
    main(sys.argv[1:])
else:
    print "name: " + __name__